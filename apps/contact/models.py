from django.db import models

from django.urls import reverse_lazy
from django.contrib import messages

from apps.company.models import Company

# People that are not employees just foreman , sub drivers, people
class Contact(models.Model):
    company = models.ForeignKey(Company, on_delete= models.CASCADE)
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    address1 = models.CharField(max_length=50, blank=True)
    address2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=25, blank=True)
    state = models.CharField(max_length=2, default='CA', blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True)
    phone_number = models.CharField(max_length=14, blank=True)
    fax = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=150, blank=True)
    social_number = models.CharField(max_length=14, blank=True)
    emergency_phone = models.CharField(max_length=14, blank=True)
    emergency_contact = models.CharField(max_length=14, blank=True)
    notes = models.TextField(null=True, blank=True)
    profile_image = models.ImageField(default='contact/default.jpg', upload_to='contact/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    class Meta(object):
        unique_together = ("firstname", "lastname")
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return '%s %s %s' % (self.company, self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse_lazy('contact-detail', args=[str(self.id)])
