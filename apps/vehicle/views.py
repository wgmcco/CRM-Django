from django.shortcuts import render

from django.views.generic import ListView, TemplateView
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


class VehicleUpdateView(LoginRequiredMixin, TemplateView):
    vehicle_form = VehicleForm
    template_name = 'common/vehicles-update.html'

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        vehicle_form = VehicleForm(post_data)

        if vehicle_form.is_valid():
            vehicle_form.save()
            messages.success(request, 'Your vehicle was updated successfully!')
            return HttpResponseRedirect(reverse_lazy('vehicles'))

        context = self.get_context_data(
                                        user_form=vehicle_form,
                                    )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)