from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, ListView
from .forms import SignUpForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls import reverse_lazy

from ..company.models import Company
from ..contact.models import Contact
from ..vehicle.models import Vehicle
from ..employee.models import Employee
from ..agency.models import Agency
from ..insurance.models import Insurance
from ..permit.models import Permit
from ..document.models import Document

class HomeView(TemplateView):
    template_name = 'common/home.html'


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'common/dashboard.html'
    login_url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        concnt = Contact.objects.count()
        comcnt = Company.objects.count()
        vehcnt = Vehicle.objects.count()
        empcnt = Employee.objects.count()
        agecnt = Agency.objects.count()
        inscnt = Insurance.objects.count()
        percnt = Permit.objects.count()
        doccnt = Document.objects.count()
        context = {
            'concnt': concnt,
            'comcnt': comcnt,
            'empcnt': empcnt,
            'agecnt': agecnt,
            'inscnt': inscnt,
            'percnt': percnt,
            'vehcnt': vehcnt,
            'doccnt': doccnt,
        }
        return render(request, 'common/dashboard.html', context)



class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'common/register.html'


from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserForm, ProfileForm
from django.contrib.auth.models import User
from apps.userprofile.models import Profile

from django.contrib import messages


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'common/profile.html'


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'common/profile-update.html'

    def post(self, request):

        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully!')
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
                                        user_form=user_form,
                                        profile_form=profile_form
                                    )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

