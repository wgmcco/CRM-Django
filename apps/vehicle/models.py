
from django.db import models
from django.urls import reverse_lazy
from django.contrib import messages
from apps.employee.utils import CATEGORY
from apps.employee.models import Employee
from apps.company.models import Company
from apps.image.models import Image


# Equipment with tires
class Vehicle(models.Model):
    equip_number = models.CharField(max_length=20, unique=True)
    category = models.CharField(max_length=2, null=True, choices=CATEGORY)
    equip_name = models.CharField(max_length=50, blank=True)
    equip_driver = models.ForeignKey(Employee, on_delete= models.CASCADE)
    model_year = models.CharField(max_length=4, blank=True)
    owner = models.ForeignKey(Company, on_delete=models.CASCADE)
    purchased_date = models.DateField(null=True, blank=True)
    vin_number = models.CharField(max_length=50, blank=True)
    license_number = models.CharField(max_length=15, blank=True)
    make = models.CharField(max_length=20, blank=True)
    model = models.CharField(max_length=150)
    width = models.CharField(max_length=150)
    length = models.CharField(max_length=150)
    image_image = models.ManyToManyField(Image, blank=True)
    profile_image = models.ImageField(default='equipment/default.jpg', upload_to='equipment/', null=True, blank=True)
    note = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.equip_number

    def get_absolute_url(self):
        return reverse_lazy('vehicle-detail', args=[str(self.id)])

