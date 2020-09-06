from django.shortcuts import render, get_object_or_404
from django.template import context

from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView
from .models import Employee
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy


class EmployeeAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'employee/employee-add.html'
    model = Employee
    success_message = "Employee was added successfully"
    fields = '__all__'


class EmployeeView(LoginRequiredMixin, ListView):
    template_name = 'employee/employee.html'
    model = Employee
    queryset = Employee.objects.order_by('first_name','last_name')
    context_object_name = "employee"
    login_url = reverse_lazy('home')
    paginate_by = 2

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            results = Employee.objects.search(query)
            return results
        return Employee.objects.order_by('first_name', 'last_name')




class EmployeeDetailView(LoginRequiredMixin, DetailView):
    template_name = 'employee/employee-detail.html'
    model = Employee
    context_object_name = "employee"
    login_url = reverse_lazy('home')


class EmployeeUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'employee/employee-update.html'
    model = Employee
    success_message = "Employee was updated successfully"
    fields = '__all__'

