from django.shortcuts import render, get_object_or_404
from django.template import context

from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView
from .models import Document
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy


class DocumentAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'common/document-add.html'
    model = Document
    success_message = "Document was added successfully"
    fields = '__all__'


class DocumentView(LoginRequiredMixin, ListView):
    template_name = 'common/document.html'
    model = Document
    queryset = Document.objects.order_by('company')
    context_object_name = "document"
    login_url = reverse_lazy('home')


class DocumentDetailView(LoginRequiredMixin, DetailView):
    template_name = 'common/document-detail.html'
    model = Document
    context_object_name = "document"
    login_url = reverse_lazy('home')


class DocumentUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'common/document-update.html'
    model = Document
    success_message = "Document was updated successfully"
    success_url = '/document'
    fields = '__all__'