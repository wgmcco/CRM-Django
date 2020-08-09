from django.db import models
from apps.employee.utils import DOCUMENT_TYPE
from django.urls import reverse_lazy
from apps.company.models import Company
from django.contrib import messages


class Document(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    type = models.CharField(max_length=3, choices=DOCUMENT_TYPE)
    start_date = models.DateField()
    end_date = models.DateField()
    pdf = models.FileField(upload_to='document/', blank=True, null=True)
    note = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta(object):
        verbose_name = "Document"
        verbose_name_plural = "Documents"

    def __str__(self):
        return '%s - %s' % (self.company, self.type)

    def get_absolute_url(self):
        return reverse_lazy('document-detail', args=[str(self.id)])
