from django.urls import path, include
from .views import PermitView, PermitAddView, PermitDetailView, PermitUpdateView


urlpatterns = [
    path('', PermitView.as_view(), name='permit'),
    path('permit-detail/<int:pk>', PermitDetailView.as_view(), name='permit-detail'),
    path('permit-update/<int:pk>', PermitUpdateView.as_view(), name='permit-update'),
    path('permit-add/', PermitAddView.as_view(), name='permit-add')
]