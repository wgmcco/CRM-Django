from django.shortcuts import render, get_object_or_404
from django.template import context

from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView
from .models import Vehicle
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy


class VehicleView(LoginRequiredMixin, ListView):
    template_name = 'common/vehicles.html'
    model = Vehicle
    context_object_name = "vehicle"
    login_url = reverse_lazy('home')


class VehicleDetailView(LoginRequiredMixin, DetailView):
    template_name = 'common/vehicles-detail.html'
    model = Vehicle
    context_object_name = "vehicle"
    login_url = reverse_lazy('home')


class VehicleAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'common/vehicles-add.html'
    model = Vehicle
    success_message = "Vehicle was added successfully"
    fields = '__all__'


class VehicleUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'common/vehicle-update.html'
    model = Vehicle
    success_message = "Vehicle was updated successfully"
    fields = '__all__'

