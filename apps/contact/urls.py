from django.urls import path, include
from .views import ContactAddView, ContactDetailView, ContactUpdateView, ContactView


urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
    path('contact-detail/<int:pk>', ContactDetailView.as_view(), name='contact-detail'),
    path('contact-update/<int:pk>', ContactUpdateView.as_view(), name='contact-update'),
    path('contact-add/', ContactAddView.as_view(), name='contact-add')
]