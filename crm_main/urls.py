
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from apps.vehicle.views import VehicleView, VehicleDetailView, VehicleAddView, VehicleUpdateView
from apps.employee.views import EmployeeAddView, EmployeeView, EmployeeDetailView, EmployeeUpdateView
from apps.contact.views import ContactAddView, ContactView, ContactDetailView, ContactUpdateView
from apps.agency.views import AgencyAddView, AgencyView, AgencyDetailView, AgencyUpdateView, SearchView
from apps.company.views import CompanyAddView, CompanyView, CompanyDetailView, CompanyUpdateView
from apps.document.views import DocumentView, DocumentAddView, DocumentDetailView, DocumentUpdateView
from apps.image.views import ImageView, ImageAddView, ImageDetailView, ImageUpdateView
from apps.permit.views import PermitView, PermitAddView, PermitDetailView, PermitUpdateView
from apps.insurance.views import InsuranceView, InsuranceAddView, InsuranceDetailView, InsuranceUpdateView
from apps.common.views import HomeView, SignUpView, DashboardView, ProfileUpdateView, ProfileView


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', HomeView.as_view(), name='home'),
    path('register/', SignUpView.as_view(), name='register'),
    path('vehicle/', VehicleView.as_view(), name='vehicles'),
    path('employee/', EmployeeView.as_view(), name='employee'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('agency/', AgencyView.as_view(), name='agency'),
    path('view/', SearchView.as_view(), name='search'),
    path('company/', CompanyView.as_view(), name='company'),
    path('document/', DocumentView.as_view(), name='document'),
    path('image/', ImageView.as_view(), name='image'),
    path('permit/', PermitView.as_view(), name='permit'),
    path('insurance/', InsuranceView.as_view(), name='insurance'),
    path('vehicle-detail/<int:pk>', VehicleDetailView.as_view(), name='vehicle-detail'),
    path('employee-detail/<int:pk>', EmployeeDetailView.as_view(), name='employee-detail'),
    path('contact-detail/<int:pk>', ContactDetailView.as_view(), name='contact-detail'),
    path('agency-detail/<int:pk>', AgencyDetailView.as_view(), name='agency-detail'),
    path('company-detail/<int:pk>', CompanyDetailView.as_view(), name='company-detail'),
    path('document-detail/<int:pk>', DocumentDetailView.as_view(), name='document-detail'),
    path('image-detail/<int:pk>', ImageDetailView.as_view(), name='image-detail'),
    path('insurance-detail/<int:pk>', InsuranceDetailView.as_view(), name='insurance-detail'),
    path('permit-detail/<int:pk>', PermitDetailView.as_view(), name='permit-detail'),
    path('vehicle-update/<int:pk>', VehicleUpdateView.as_view(), name='vehicle-update'),
    path('employee-update/<int:pk>', EmployeeUpdateView.as_view(), name='employee-update'),
    path('permit-update/<int:pk>', PermitUpdateView.as_view(), name='permit-update'),
    path('insurance-update/<int:pk>', InsuranceUpdateView.as_view(), name='insurance-update'),
    path('contact-update/<int:pk>', ContactUpdateView.as_view(), name='contact-update'),
    path('agency-update/<int:pk>', AgencyUpdateView.as_view(), name='agency-update'),
    path('company-update/<int:pk>', CompanyUpdateView.as_view(), name='company-update'),
    path('document-update/<int:pk>', DocumentUpdateView.as_view(), name='document-update'),
    path('image-update/<int:pk>', ImageUpdateView.as_view(), name='image-update'),
    path('vehicle-add/', VehicleAddView.as_view(), name='vehicle-add'),
    path('permit-add/', PermitAddView.as_view(), name='permit-add'),
    path('employee-add/', EmployeeAddView.as_view(), name='employee-add'),
    path('contact-add/', ContactAddView.as_view(), name='contact-add'),
    path('agency-add/', AgencyAddView.as_view(), name='agency-add'),
    path('company-add/', CompanyAddView.as_view(), name='company-add'),
    path('document-add/', DocumentAddView.as_view(), name='document-add'),
    path('image-add/', ImageAddView.as_view(), name='image-add'),
    path('insurance-add/', InsuranceAddView.as_view(), name='insurance-add'),
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