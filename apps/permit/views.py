from django.shortcuts import render, get_object_or_404
from django.template import context

from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView
from .models import Permit
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy


class PermitAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'permit/permit-add.html'
    model = Permit
    queryset = Permit.objects.order_by('permit_cn')
    success_message = "Permit was added successfully"
    fields = '__all__'


class PermitView(LoginRequiredMixin, ListView):
    template_name = 'permit/permit.html'
    model = Permit
    context_object_name = "permit"
    login_url = reverse_lazy('home')
    paginate_by = 12

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            results = Permit.objects.search(query)
            return results
        return Permit.objects.order_by('permit_cn')



class PermitDetailView(LoginRequiredMixin, DetailView):
    template_name = 'permit/permit-detail.html'
    model = Permit
    context_object_name = "permit"
    login_url = reverse_lazy('home')


class PermitUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'permit/permit-update.html'
    model = Permit
    success_message = "Permit was updated successfully"
    fields = '__all__'