from django.urls import path, include
from .views import ImageView, ImageAddView, ImageDetailView, ImageUpdateView


urlpatterns = [
    path('', ImageView.as_view(), name='image'),
    path('image-detail/<int:pk>', ImageDetailView.as_view(), name='image-detail'),
    path('image-update/<int:pk>', ImageUpdateView.as_view(), name='image-update'),
    path('image-add/', ImageAddView.as_view(), name='image-add')
]