from django.shortcuts import render, get_object_or_404
from django.template import context

from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView
from .models import Insurance
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy


class InsuranceAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'common/insurance-add.html'
    model = Insurance
    success_message = "Insurance was added successfully"
    fields = '__all__'


class InsuranceView(LoginRequiredMixin, ListView):
    template_name = 'common/insurance.html'
    model = Insurance
    context_object_name = "insurance"
    login_url = reverse_lazy('home')


class InsuranceDetailView(LoginRequiredMixin, DetailView):
    template_name = 'common/insurance-detail.html'
    model = Insurance
    context_object_name = "insurance"
    login_url = reverse_lazy('home')


class InsuranceUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'common/insurance-update.html'
    model = Insurance
    success_message = "Insurance was updated successfully"
    fields = '__all__'