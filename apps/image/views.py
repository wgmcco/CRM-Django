from django.shortcuts import render, get_object_or_404
from django.template import context

from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView
from .models import Image
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy


class ImageView(LoginRequiredMixin, ListView):
    template_name = 'image/image.html'
    model = Image
    queryset = Image.objects.order_by('equip_number')
    # queryset = Agency.objects.order_by('agency_name')
    context_object_name = "image"
    login_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            results = Image.objects.search(query)
            return results
        return Image.objects.order_by('equip_number')


class ImageDetailView(LoginRequiredMixin, DetailView):
    template_name = 'image/image-detail.html'
    model = Image
    context_object_name = "image"
    login_url = reverse_lazy('home')


class ImageAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'image/image-add.html'
    model = Image
    success_message = "Image was added successfully"
    fields = '__all__'


class ImageUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'image/image-update.html'
    model = Image
    success_message = "Image was updated successfully"
    fields = '__all__'
