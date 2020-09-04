from django.urls import path
from .views import DocumentView, DocumentUpdateView, DocumentDetailView, DocumentAddView


urlpatterns = [
    path('', DocumentView.as_view(), name='document'),
    path('document-detail/<int:pk>', DocumentDetailView.as_view(), name='document-detail'),
    path('document-update/<int:pk>', DocumentUpdateView.as_view(), name='document-update'),
    path('document-add/', DocumentAddView.as_view(), name='document-add')
]