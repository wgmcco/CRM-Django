from django.shortcuts import render, get_object_or_404
from django.template import context

from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView
from .models import Image
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy


class ImageView(LoginRequiredMixin, ListView):
    template_name = 'image/image.html'
    model = Image
    queryset = Image.objects.order_by('equip_number')
    context_object_name = "image"
    login_url = reverse_lazy('home')
    paginate_by = 9

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


class ImageDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    template_name = 'image/image-delete.html'
    model = Image
    success_message = "Image was deleted successfully"
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('image')

