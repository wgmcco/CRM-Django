from django.shortcuts import render, get_object_or_404
from django.template import context

from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView
from .models import Company
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy


class CompanyAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'company/company-add.html'
    model = Company
    success_message = "Company was added successfully"
    fields = '__all__'


class CompanyView(LoginRequiredMixin, ListView):
    template_name = 'company/company.html'
    model = Company
    queryset = Company.objects.order_by('name')
    context_object_name = "company"
    login_url = reverse_lazy('home')


class CompanyDetailView(LoginRequiredMixin, DetailView):
    template_name = 'company/company-detail.html'
    model = Company
    context_object_name = "company"
    login_url = reverse_lazy('home')


class CompanyUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'company/company-update.html'
    model = Company
    success_message = "Company was updated successfully"
    fields = '__all__'


class CompanyTemplateView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = 'company/dashboard.html'
    model = Company
    fields = '__all__'