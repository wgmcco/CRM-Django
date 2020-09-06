from django.shortcuts import render, get_object_or_404
from django.template import context
from django.core.files.storage import FileSystemStorage
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView
from .models import Document
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy


class DocumentAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'document/document-add.html'
    model = Document
    success_message = "Document was added successfully"
    fields = '__all__'


class DocumentView(LoginRequiredMixin, ListView):
    template_name = 'document/document.html'
    model = Document
    queryset = Document.objects.order_by('company')
    context_object_name = "document"
    login_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            results = Document.objects.search(query)
            return results
        return Document.objects.order_by('company')


class DocumentDetailView(LoginRequiredMixin, DetailView):
    template_name = 'document/document-detail.html'
    model = Document
    context_object_name = "document"
    login_url = reverse_lazy('home')


class DocumentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'document/document-update.html'
    model = Document
    success_message = "Document was updated successfully"
    success_url = '/document'
    fields = '__all__'