from django.urls import path, include
from .views import InsuranceUpdateView, InsuranceDetailView, InsuranceAddView, InsuranceView


urlpatterns = [
    path('', InsuranceView.as_view(), name='insurance'),
    path('insurance-detail/<int:pk>', InsuranceDetailView.as_view(), name='insurance-detail'),
    path('insurance-update/<int:pk>', InsuranceUpdateView.as_view(), name='insurance-update'),
    path('insurance-add/', InsuranceAddView.as_view(), name='insurance-add')
]