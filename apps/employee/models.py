
from django.db import models
from .utils import STATE, CLASS
from django.urls import reverse_lazy
from django.contrib import messages

from ..company.models import Company

# Hired people only
class Employee(models.Model):
    company = models.ForeignKey(Company, on_delete= models.CASCADE)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    address1 = models.CharField(max_length=50, blank=True)
    address2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=25, blank=True)
    state = models.CharField(max_length=2, choices=STATE, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True)
    phone_number = models.CharField(max_length=14, blank=True)
    emergency_phone = models.CharField(max_length=14, blank=True)
    emergency_contact = models.CharField(max_length=14, blank=True)
    social_number = models.CharField(max_length=14, blank=True)
    dob = models.DateField(null=True, blank=True)
    hire_date = models.DateField(null=True, blank=True)
    separation_date = models.DateField(null=True, blank=True)
    cdl = models.CharField(max_length=12, blank=True)
    cdl_expires = models.DateField(null=True, blank=True)
    cdl_class = models.CharField(max_length=1, choices=CLASS, blank=True, null=True)
    med_expires = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(default='equipment/default.jpg', upload_to='equipment/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta(object):
        unique_together = ("first_name", "last_name")

    def __str__(self):
        return '%s %s %s' % (self.company, self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse_lazy('employee-detail', args=[str(self.id)])


