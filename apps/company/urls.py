from django.urls import path, include
from .views import CompanyAddView, CompanyDetailView, CompanyUpdateView, CompanyView


urlpatterns = [
    path('', CompanyView.as_view(), name='company'),
    path('company-detail/<int:pk>', CompanyDetailView.as_view(), name='company-detail'),
    path('company-update/<int:pk>', CompanyUpdateView.as_view(), name='company-update'),
    path('company-add/', CompanyAddView.as_view(), name='company-add')
]