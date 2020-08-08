from django.db import models
from apps.employee.utils import TYPE
from django.urls import reverse_lazy
from apps.contact.models import Contact
from apps.vehicle.models import Vehicle
from apps.company.models import Company
from apps.agency.models import Agency
from django.contrib import messages

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

	class Meta(object):
		verbose_name = "Permit"
		verbose_name_plural = "Permits"

	def __str__(self):
		return self.permit_cn

	def get_absolute_url(self):
		return reverse_lazy('permit-detail', args=[str(self.id)])