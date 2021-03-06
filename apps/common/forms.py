from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from apps.userprofile.models import Profile
from apps.vehicle.models import Vehicle


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Enter a valid email address')

    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
            ]


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'bio',
            'phone_number',
            'birth_date',
            'social_number',
            'profile_image'
            ]
        widgets = {'social_number': forms.TextInput(attrs={'data-mask': "000-00-0000"})}


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = [
            'equip_number',
            'equip_name',
            'equip_driver',
            'purchased_date',
            'vin_number',
            'license_number',
            'make',
            'profile_image'
            ]


