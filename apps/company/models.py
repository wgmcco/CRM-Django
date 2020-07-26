
from django.db import models
from apps.employee.utils import STATE, INCORPORATED
from django.urls import reverse_lazy
from django.contrib import messages


class Company(models.Model):
    name = models.CharField(max_length=100, blank=True)
    address1 = models.CharField(max_length=50, blank=True)
    address2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=25, blank=True)
    state = models.CharField(max_length=2, choices=STATE, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True)
    phone_number = models.CharField(max_length=14, blank=True)
    fax_phone = models.CharField(max_length=14, blank=True)
    type = models.CharField(max_length=1, choices=INCORPORATED, blank=True, null=True)
    notes = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(default='company/default.jpg', upload_to='company/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('company-detail', args=[str(self.id)])