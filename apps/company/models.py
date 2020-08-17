
from django.db import models
from apps.employee.utils import STATE, INCORPORATED, COMPANY_TYPE
from django.urls import reverse_lazy
#from apps.contact.models import Contact
from django.contrib import messages
from django.db.models import Q


class PostManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(name__icontains=query) |
                         Q(company_type__icontains=query) |
                         Q(city__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs

# Companies both Vendors & Subs
class Company(models.Model):
    name = models.CharField(max_length=100, blank=True)
    company_type = models.CharField(max_length=1, choices=COMPANY_TYPE, blank=True, null=True)
    address1 = models.CharField(max_length=50, blank=True)
    address2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=25, blank=True)
    state = models.CharField(max_length=2, choices=STATE, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True)
    phone_number = models.CharField(max_length=14, blank=True)
    fax_phone = models.CharField(max_length=14, blank=True)
    owner = models.CharField(max_length=45, blank=True)
    contacts = models.ManyToManyField('contact.Contact', blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True)
    type = models.CharField(max_length=1, choices=INCORPORATED, blank=True, null=True)
    notes = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(default='company/default.jpg', upload_to='company/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = PostManager()

    class Meta(object):
        verbose_name = "Company"
        verbose_name_plural = "Companies"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy('company-detail', args=[str(self.id)])