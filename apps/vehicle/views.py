from django.shortcuts import render

from django.views.generic import ListView
from .models import Vehicle
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy


class VehicleView(LoginRequiredMixin, ListView):
    template_name = 'common/vehicles.html'
    model = Vehicle
    context_object_name = "vehicle"
    login_url = reverse_lazy('home')