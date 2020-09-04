from django.urls import path, include
from .views import VehicleAddView, VehicleUpdateView, VehicleView, vehicle_detail_view


urlpatterns = [
    path('', VehicleView.as_view(), name='vehicles'),
    path('vehicle-detail/<int:pk>', vehicle_detail_view,name='vehicle-detail'),
    path('vehicle-update/<int:pk>', VehicleUpdateView.as_view(), name='vehicle-update'),
    path('vehicle-add/', VehicleAddView.as_view(), name='vehicle-add')
]