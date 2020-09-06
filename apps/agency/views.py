from django.shortcuts import render, get_object_or_404
from django.template import context
from django.db.models import Q
from itertools import chain
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView
from .models import Agency
from apps.contact.models import Contact
from apps.company.models import Company
from apps.image.models import Image
from apps.employee.models import Employee
from apps.vehicle.models import Vehicle
from apps.permit.models import Permit
from apps.insurance.models import Insurance
from apps.document.models import Document
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy


class AgencyView(LoginRequiredMixin, ListView):
    template_name = 'agency/agency.html'
    model = Agency
    queryset = Agency.objects.order_by('agency_name')
    context_object_name = "agency"
    login_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            results = Agency.objects.search(query)
            return results
        return Agency.objects.order_by('agency_name')


class AgencyDetailView(LoginRequiredMixin, DetailView):
    template_name = 'agency/agency-detail.html'
    model = Agency
    context_object_name = "agency"
    login_url = reverse_lazy('home')


class AgencyAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'agency/agency-add.html'
    model = Agency
    success_message = "Agency was added successfully"
    fields = '__all__'


class AgencyUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'agency/agency-update.html'
    model = Agency
    success_message = "Agency was updated successfully"
    fields = '__all__'


class SearchView(ListView):

    template_name = 'common/view.html'
    paginate_by = 200
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
            agency_results = Agency.objects.search(query)
            contact_results = Contact.objects.search(query)
            company_results = Company.objects.search(query)
            image_results = Image.objects.search(query)
            employee_results = Employee.objects.search(query)
            vehicle_results = Vehicle.objects.search(query)
            permit_results = Permit.objects.search(query)
            insurance_results = Insurance.objects.search(query)
            documents_results = Document.objects.search(query)

            # combine query sets
            queryset_chain = chain(
                agency_results,
                contact_results,
                company_results,
                image_results,
                employee_results,
                vehicle_results,
                permit_results,
                insurance_results,
                documents_results
            )
            qs = sorted(queryset_chain,
                        key=lambda instance: instance.pk,
                        reverse=True)
            self.count = len(qs)  # since qs is actually a list
            return qs
        return Agency.objects.none()  # just an empty queryset as default


