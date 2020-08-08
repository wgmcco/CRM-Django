from django.shortcuts import render, get_object_or_404
from django.template import context

from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView
from .models import Permit
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy


class PermitAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'common/permit-add.html'
    model = Permit
    success_message = "Permit was added successfully"
    fields = '__all__'


class PermitView(LoginRequiredMixin, ListView):
    template_name = 'common/permit.html'
    model = Permit
    context_object_name = "permit"
    login_url = reverse_lazy('home')


class PermitDetailView(LoginRequiredMixin, DetailView):
    template_name = 'common/permit-detail.html'
    model = Permit
    context_object_name = "permit"
    login_url = reverse_lazy('home')


class PermitUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'common/permit-update.html'
    model = Permit
    success_message = "Permit was updated successfully"
    fields = '__all__'