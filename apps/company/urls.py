from django.urls import path, include
from .views import CompanyAddView, CompanyDetailView, CompanyUpdateView, CompanyView, companycsv, render_pdf_view


urlpatterns = [
    path('', CompanyView.as_view(), name='company'),
    path('company-detail/<int:pk>', CompanyDetailView.as_view(), name='company-detail'),
    path('company-update/<int:pk>', CompanyUpdateView.as_view(), name='company-update'),
    path('company-add/', CompanyAddView.as_view(), name='company-add'),
    path('company-csv/',companycsv, name='company-csv'),
    path('company-pdf/<int:pk>',render_pdf_view, name='company-pdf')
]