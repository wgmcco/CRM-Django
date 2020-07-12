from django.shortcuts import render, get_object_or_404
from django.template import context

from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView
from .models import Vehicle
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.urls import reverse_lazy

from ..common.forms import VehicleForm


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


class AddVehicleView(LoginRequiredMixin, CreateView):
    template_name = 'common/vehicles-add.html'
    model = Vehicle
    fields = '__all__'
