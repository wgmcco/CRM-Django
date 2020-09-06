from django.shortcuts import render, get_object_or_404
from django.template import context

from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView
from .models import Insurance
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy


class InsuranceAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'insurance/insurance-add.html'
    model = Insurance
    success_message = "Insurance was added successfully"
    fields = '__all__'


class InsuranceView(LoginRequiredMixin, ListView):
    template_name = 'insurance/insurance.html'
    model = Insurance
    queryset = Insurance.objects.order_by('company')
    context_object_name = "insurance"
    login_url = reverse_lazy('home')
    paginate_by = 3

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            results = Insurance.objects.search(query)
            return results
        return Insurance.objects.order_by('company')


class InsuranceDetailView(LoginRequiredMixin, DetailView):
    template_name = 'insurance/insurance-detail.html'
    model = Insurance
    context_object_name = "insurance"
    login_url = reverse_lazy('home')


class InsuranceUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'insurance/insurance-update.html'
    model = Insurance
    success_message = "Insurance was updated successfully"
    fields = '__all__'