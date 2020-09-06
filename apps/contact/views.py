from django.shortcuts import render, get_object_or_404
from django.template import context

from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView
from .models import Contact
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy


class ContactView(LoginRequiredMixin, ListView):
    template_name = 'contact/contact.html'
    model = Contact
    queryset = Contact.objects.order_by('com')
    context_object_name = "contact"
    login_url = reverse_lazy('home')
    paginate_by = 12


    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            results = Contact.objects.search(query)
            return results
        return Contact.objects.order_by('com')


class ContactDetailView(LoginRequiredMixin, DetailView):
    template_name = 'contact/contact-detail.html'
    model = Contact
    context_object_name = "contact"
    login_url = reverse_lazy('home')


class ContactAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'contact/contact-add.html'
    model = Contact
    success_message = "Contact was added successfully"
    fields = '__all__'


class ContactUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'contact/contact-update.html'
    model = Contact
    success_message = "Contact was updated successfully"
    fields = '__all__'
