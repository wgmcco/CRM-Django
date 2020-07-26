from django.shortcuts import render, get_object_or_404
from django.template import context

from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView
from .models import Contact
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy


class ContactView(LoginRequiredMixin, ListView):
    template_name = 'common/contact.html'
    model = Contact
    context_object_name = "contact"
    login_url = reverse_lazy('home')


class ContactDetailView(LoginRequiredMixin, DetailView):
    template_name = 'common/contact-detail.html'
    model = Contact
    context_object_name = "contact"
    login_url = reverse_lazy('home')


class ContactAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'common/contact-add.html'
    model = Contact
    success_message = "Contact was added successfully"
    fields = '__all__'


class ContactUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'common/contact-update.html'
    model = Contact
    success_message = "Contact was updated successfully"
    fields = '__all__'
