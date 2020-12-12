from django.urls import path, include
from .views import CompanyAddView, CompanyDetailView, CompanyUpdateView, CompanyView, companycsv, render_pdf_view
from apps.common.views import SummaryView



urlpatterns = [
    path('', CompanyView.as_view(), name='company'),
    path('company-detail/<int:pk>', CompanyDetailView.as_view(), name='company-detail'),
    path('company-update/<int:pk>', CompanyUpdateView.as_view(), name='company-update'),
    path('company-add/', CompanyAddView.as_view(), name='company-add'),
    path('company-csv/<int:pk>',companycsv, name='company-csv'),
    path('company-pdf/<int:pk>',render_pdf_view, name='company-pdf'),
    path('company-summary/<int:pk>', SummaryView.as_view(), name='company-summary'),
]