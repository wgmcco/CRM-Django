from django.urls import path
from .views import AgencyView, AgencyDetailView, AgencyAddView, AgencyUpdateView


urlpatterns = [
    path('', AgencyView.as_view(), name='agency'),
    path('agency-detail/<int:pk>', AgencyDetailView.as_view(), name='agency-detail'),
    path('agency-update/<int:pk>', AgencyUpdateView.as_view(), name='agency-update'),
    path('agency-add/', AgencyAddView.as_view(), name='agency-add')
]