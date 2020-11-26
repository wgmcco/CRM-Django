
from django.db import models
from .utils import STATE, CLASS
from django.urls import reverse_lazy
from django.contrib import messages
from ..company.models import Company
from django.db.models import Q


class PostManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(company__name__icontains=query) |
                         Q(first_name__icontains=query) |
                         Q(last_name__icontains=query) |
                         Q(address1__icontains=query) |
                         Q(address2__icontains=query) |
                         Q(city__icontains=query) |
                         Q(state__icontains=query) |
                         Q(zip_code__icontains=query) |
                         Q(phone_number__icontains=query) |
                         Q(emergency_phone__icontains=query) |
                         Q(emergency_contact__icontains=query) |
                         Q(social_number__icontains=query) |
                         Q(dob__icontains=query) |
                         Q(hire_date__icontains=query) |
                         Q(cdl_expires__icontains=query) |
                         Q(notes__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs

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
    profile_image = models.ImageField(default='employee/default.jpg', upload_to='employee/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    objects = PostManager()

    class Meta(object):
        unique_together = ("first_name", "last_name")

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse_lazy('employee-detail', args=[str(self.id)])


