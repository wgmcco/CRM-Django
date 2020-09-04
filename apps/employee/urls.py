from django.urls import path, include
from .views import EmployeeView, EmployeeAddView, EmployeeDetailView, EmployeeUpdateView


urlpatterns = [
    path('', EmployeeView.as_view(), name='employee'),
    path('employee-detail/<int:pk>', EmployeeDetailView.as_view(), name='employee-detail'),
    path('employee-update/<int:pk>', EmployeeUpdateView.as_view(), name='employee-update'),
    path('employee-add/', EmployeeAddView.as_view(), name='employee-add')
]