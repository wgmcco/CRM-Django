from django.db import models
from apps.employee.utils import TYPE
from django.urls import reverse_lazy
from apps.contact.models import Contact
from apps.vehicle.models import Vehicle
from apps.company.models import Company
from apps.agency.models import Agency
from django.db.models import Q
from django.contrib import messages


class PostManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(permit_cn__icontains=query) |
                         Q(agency__agency_name__icontains=query) |
                         Q(agency_type__icontains=query) |
                         Q(company__name__icontains=query) |
                         Q(valid_from__icontains=query) |
                         Q(valid_to__icontains=query) |
                         Q(permit_class__icontains=query) |
                         Q(vehicle__equip_number__icontains=query) |
                         Q(loaded_height__icontains=query) |
                         Q(loaded_width__icontains=query) |
                         Q(note__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs


# Transportation Permits
class Permit(models.Model):
    permit_cn = models.CharField("Permit number", max_length=150, unique=True)
    agency = models.ForeignKey(Agency, on_delete=models.PROTECT)
    agency_type = models.CharField(max_length=2, choices=TYPE, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    valid_from = models.DateField()
    valid_to = models.DateField()
    permit_class = models.CharField(max_length=40)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    loaded_height = models.CharField(max_length=150)
    loaded_width = models.CharField(max_length=150)
    pdf = models.FileField(upload_to='pdfs/', blank=True)
    note = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = PostManager()

    class Meta(object):
        verbose_name = "Permit"
        verbose_name_plural = "Permits"

    def __str__(self):
        return self.permit_cn

    def get_absolute_url(self):
        return reverse_lazy('permit-detail', args=[str(self.id)])
