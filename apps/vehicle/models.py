
from django.db import models
from django.urls import reverse



class Vehicle(models.Model):
    equip_number = models.CharField(max_length=20, blank=True)
    equip_name = models.CharField(max_length=50, blank=True)
    equip_driver = models.CharField(max_length=50, blank=True)
    purchased_date = models.DateField(null=True, blank=True)
    vin_number = models.CharField(max_length=50, blank=True)
    license_number = models.CharField(max_length=15, blank=True)
    make = models.CharField(max_length=20, blank=True)
    profile_image = models.ImageField(default='equipment/default.jpg', upload_to='equipment/', null=True, blank=True)

    def __str__(self):
        return '%s %s' % (self.equip_number, self.equip_name)

    def get_absolute_url(self):
        return reverse('vehicle-detail', args=[str(self.id)])
