
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from apps.vehicle.views import VehicleView, VehicleDetailView, VehicleAddView, VehicleUpdateView
from apps.employee.views import EmployeeAddView, EmployeeView, EmployeeDetailView, EmployeeUpdateView
from apps.contact.views import ContactAddView, ContactView, ContactDetailView, ContactUpdateView
from apps.agency.views import AgencyAddView, AgencyView, AgencyDetailView, AgencyUpdateView
from apps.common.views import HomeView, SignUpView, DashboardView, ProfileUpdateView, ProfileView


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', HomeView.as_view(), name='home'),
    path('register/', SignUpView.as_view(), name='register'),
    path('vehicle/', VehicleView.as_view(), name='vehicles'),
    path('employee/', EmployeeView.as_view(), name='employee'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('agency/', AgencyView.as_view(), name='agency'),
    path('vehicle-detail/<int:pk>', VehicleDetailView.as_view(), name='vehicle-detail'),
    path('employee-detail/<int:pk>', EmployeeDetailView.as_view(), name='employee-detail'),
    path('contact-detail/<int:pk>', ContactDetailView.as_view(), name='contact-detail'),
    path('agency-detail/<int:pk>', AgencyDetailView.as_view(), name='agency-detail'),
    path('vehicle-update/<int:pk>', VehicleUpdateView.as_view(), name='vehicle-update'),
    path('employee-update/<int:pk>', EmployeeUpdateView.as_view(), name='employee-update'),
    path('contact-update/<int:pk>', ContactUpdateView.as_view(), name='contact-update'),
    path('agency-update/<int:pk>', AgencyUpdateView.as_view(), name='agency-update'),
    path('vehicle-add/', VehicleAddView.as_view(), name='vehicle-add'),
    path('employee-add/', EmployeeAddView.as_view(), name='employee-add'),
    path('contact-add/', ContactAddView.as_view(), name='contact-add'),
    path('agency-add/', AgencyAddView.as_view(), name='agency-add'),

    path('login/', auth_views.LoginView.as_view(
        template_name='common/login.html'
        ),
        name='login'),

    path('logout/', auth_views.LogoutView.as_view(
        next_page='home'
    ),
         name='logout'),

    path('dashboard/', DashboardView.as_view(), name='dashboard'),

    path('profile-update/', ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/', ProfileView.as_view(), name='profile'),

    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='common/change-password.html',
            success_url='/'
        ),
        name='change-password'
    ),

    # Forget Password
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='common/password-reset/password_reset.html',
             subject_template_name='common/password-reset/password_reset_subject.txt',
             email_template_name='common/password-reset/password_reset_email.html',
             # success_url='/login/'
         ),
         name='password-reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='common/password-reset/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='common/password-reset/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='common/password-reset/password_reset_complete.html'
         ),
         name='password_reset_complete'),

]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)