from django.urls import path, include
from .views import ImageView, ImageAddView, ImageDetailView, ImageUpdateView, ImageDeleteView


urlpatterns = [
    path('', ImageView.as_view(), name='image'),
    path('image-detail/<int:pk>', ImageDetailView.as_view(), name='image-detail'),
    path('image-update/<int:pk>', ImageUpdateView.as_view(), name='image-update'),
    path('image-add/', ImageAddView.as_view(), name='image-add'),
    path('image-delete/<int:pk>', ImageDeleteView.as_view(), name='image-delete')
]