from django.db import models
from apps.employee.utils import TYPE
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q


class PostManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(agency_name__icontains=query) |
                         Q(first_name__icontains=query) |
                         Q(last_name__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs


# Muni names for permits
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
    fax_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=150, default='unk@unk.com')
    website = models.CharField(max_length=200, blank=True)
    notes = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(default='agency/default.jpg', upload_to='agency/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = PostManager()

    class Meta(object):
        verbose_name = "Agency"
        verbose_name_plural = "Agencies"

    def __str__(self):
        return self.agency_name

    def get_absolute_url(self):
        return reverse_lazy('agency-detail', args=[str(self.id)])