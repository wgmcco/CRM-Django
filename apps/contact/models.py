from django.db import models
from django.urls import reverse_lazy
from django.contrib import messages
from apps.company.models import Company
from django.db.models import Q


class PostManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(city__icontains=query) |
                         Q(first_name__icontains=query) |
                         Q(last_name__icontains=query) |
                         Q(com__name__icontains=query) |
                         Q(address1__icontains=query) |
                         Q(address2__icontains=query) |
                         Q(state__icontains=query) |
                         Q(zip_code__icontains=query) |
                         Q(phone_number__icontains=query) |
                         Q(fax__icontains=query) |
                         Q(email__icontains=query) |
                         Q(social_number__icontains=query) |
                         Q(emergency_phone__icontains=query) |
                         Q(emergency_contact__icontains=query) |
                         Q(notes__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs


# People that are not employees just foreman , sub drivers, people
class Contact(models.Model):
    com = models.ForeignKey(Company, blank=True, null=True, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=50)
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
    profile_image = models.ImageField(default='contact/default_person.png', upload_to='contact/', null=True, blank=True)
    date_created = models.DateTimeField(auto_now=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    objects = PostManager()

    class Meta(object):
        unique_together = ("first_name", "last_name")

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    def get_absolute_url(self):
        return reverse_lazy('contact-detail', args=[str(self.id)])

