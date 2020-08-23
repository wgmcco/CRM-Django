from django.shortcuts import render, get_object_or_404
from django.template import context

from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView
from .models import Image
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy


class ImageView(LoginRequiredMixin, ListView):
    template_name = 'common/image.html'
    model = Image
    queryset = Image.objects.order_by('equip_number')
    context_object_name = "image"
    login_url = reverse_lazy('home')


class ImageDetailView(LoginRequiredMixin, DetailView):
    template_name = 'common/image-detail.html'
    model = Image
    context_object_name = "image"
    login_url = reverse_lazy('home')


class ImageAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'common/image-add.html'
    model = Image
    success_message = "Image was added successfully"
    fields = '__all__'


class ImageUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'common/image-update.html'
    model = Image
    success_message = "Image was updated successfully"
    fields = '__all__'
