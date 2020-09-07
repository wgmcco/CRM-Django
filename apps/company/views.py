from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import context
import csv
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView
from .models import Company
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from django.urls import reverse_lazy


def render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    company = get_object_or_404(Company, pk=pk)

    template_path = 'company/company-pdf.html'

    context = {'company': company}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    # if down load
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if open in browser
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def companycsv(request):
    response = HttpResponse(content_type='text/csv')
    writer = csv.writer(response)
    writer.writerow(['Company Name', 'Owner Name', 'Phone Number', 'Notes'])

    for company in Company.objects.all().values_list('name', 'owner', 'phone_number', 'notes'):
        writer.writerow(company)
    response['Content-Disposition'] = 'attachment; filename="company.csv"'

    return response


class CompanyAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    template_name = 'company/company-add.html'
    model = Company
    success_message = "Company was added successfully"
    fields = '__all__'


class CompanyView(LoginRequiredMixin, ListView):
    template_name = 'company/company.html'
    model = Company
    queryset = Company.objects.order_by('name')
    context_object_name = "company"
    login_url = reverse_lazy('home')
    paginate_by = 10

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['query'] = self.request.GET.get('q')
        return context

    def get_queryset(self):
        request = self.request
        query = request.GET.get('q', None)

        if query is not None:
            results = Company.objects.search(query)
            return results
        return Company.objects.order_by('name')


class CompanyDetailView(LoginRequiredMixin, DetailView):
    template_name = 'company/company-detail.html'
    model = Company
    context_object_name = "company"
    login_url = reverse_lazy('home')


class CompanyUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'company/company-update.html'
    model = Company
    success_message = "Company was updated successfully"
    fields = '__all__'


class CompanyTemplateView(LoginRequiredMixin, SuccessMessageMixin, TemplateView):
    template_name = 'company/dashboard.html'
    model = Company
    fields = '__all__'