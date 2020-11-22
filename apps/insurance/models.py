from django.db import models
from apps.employee.utils import INSURANCE_TYPE
from django.urls import reverse_lazy
from apps.company.models import Company
from django.contrib import messages
from django.db.models import Q


class PostManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(type__icontains=query) |
                         Q(company__name__icontains=query) |
                         Q(start_date__icontains=query) |
                         Q(end_date__icontains=query) |
                         Q(note__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs


class Insurance(models.Model):
    type = models.CharField(max_length=2, choices=INSURANCE_TYPE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    pdf = models.FileField(default="pdfs/default.pdf", upload_to='pdfs/')
    note = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = PostManager()

    class Meta(object):
        unique_together = ("company", "type")
        verbose_name = "Insurance"
        verbose_name_plural = "Insurance"

    def __str__(self):
        return '%s - %s' % (self.company, self.type)

    def get_absolute_url(self):
        return reverse_lazy('insurance-detail', args=[str(self.id)])
