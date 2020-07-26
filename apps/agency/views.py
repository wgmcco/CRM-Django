from django.shortcuts import render, get_object_or_404
from django.template import context

from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView
from .models import Agency
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy


class AgencyView(LoginRequiredMixin, ListView):
    template_name = 'common/agency.html'
    model = Agency
    context_object_name = "agency"
    login_url = reverse_lazy('home')


class AgencyDetailView(LoginRequiredMixin, DetailView):
    template_name = 'common/agency-detail.html'
    model = Agency
    context_object_name = "agency"
    login_url = reverse_lazy('home')


class AgencyAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'common/contact-add.html'
    model = Agency
    success_message = "Agency was added successfully"
    fields = '__all__'


class AgencyUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'common/agency-update.html'
    model = Agency
    success_message = "Agency was updated successfully"
    fields = '__all__'


