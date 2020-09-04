from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from apps.agency.views import SearchView
from apps.common.views import HomeView, SignUpView, DashboardView, ProfileUpdateView, ProfileView


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', HomeView.as_view(), name='home'),
    path('register/', SignUpView.as_view(), name='register'),

    path('vehicle/', include('apps.vehicle.urls')),
    path('employee/', include('apps.employee.urls')),
    path('image/', include('apps.image.urls')),
    path('contact/', include('apps.contact.urls')),
    path('agency', include('apps.agency.urls')),
    path('company/', include('apps.company.urls')),
    path('document/', include('apps.document.urls')),
    path('permit/', include('apps.permit.urls')),
    path('insurance/', include('apps.insurance.urls')),

    path('view/', SearchView.as_view(), name='search'),

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