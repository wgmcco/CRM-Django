from django.db import models
from apps.employee.utils import TYPE
from django.urls import reverse_lazy
from django.contrib import messages


class Agency(models.Model):
    agency_name = models.CharField(max_length=50, blank=True)
    agency_type = models.CharField(max_length=2, choices=TYPE, blank=True, null=True)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    address1 = models.CharField(max_length=50, blank=True)
    address2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=25, blank=True)
    state = models.CharField(max_length=2, default='CA', blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True)
    phone_number = models.CharField(max_length=14, blank=True)
    notes = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(default='agency/default.jpg', upload_to='agency/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.agency_name

    def get_absolute_url(self):
        return reverse_lazy('agency-detail', args=[str(self.id)])