from django.shortcuts import render, get_object_or_404
from django.template import context
from itertools import chain
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView
from .models import Agency
from apps.contact.models import Contact
from apps.company.models import Company
from apps.image.models import Image
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy


class AgencyView(LoginRequiredMixin, ListView):
    template_name = 'common/agency.html'
    model = Agency
    queryset = Agency.objects.order_by('agency_name')
    context_object_name = "agency"
    login_url = reverse_lazy('home')


class AgencyDetailView(LoginRequiredMixin, DetailView):
    template_name = 'common/agency-detail.html'
    model = Agency
    context_object_name = "agency"
    login_url = reverse_lazy('home')


class AgencyAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'common/agency-add.html'
    model = Agency
    success_message = "Agency was added successfully"
    fields = '__all__'


class AgencyUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'common/agency-update.html'
    model = Agency
    success_message = "Agency was updated successfully"
    fields = '__all__'


class SearchView(ListView):
    template_name = 'common/view.html'
    paginate_by = 20
    count = 0

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['count'] = self.count or 0
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            blog_results = Agency.objects.search(query)
            contact_results = Contact.objects.search(query)
            company_results = Company.objects.search(query)
            image_results = Image.objects.search(query)

            # combine querysets
            queryset_chain = chain(
                blog_results,
                contact_results,
                company_results,
                image_results
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs)  # since qs is actually a list
            return qs
        return Agency.objects.none()  # just an empty queryset as default


