from django.db import models
from django.urls import reverse_lazy
#from apps.vehicle.models import Vehicle
from django.db.models import Q


class PostManager(models.Manager):
    def search(self, query=None):
        qs = self.get_queryset()
        if query is not None:
            or_lookup = (Q(name__icontains=query) |
                         Q(equip_number__equip_number__icontains=query) |
                         Q(notes__icontains=query)
                        )
            qs = qs.filter(or_lookup).distinct() # distinct() is often necessary with Q lookups
        return qs


# Image Storage System
class Image(models.Model):
    name = models.CharField(max_length=100, blank=True)
    equip_number = models.ForeignKey('vehicle.Vehicle', on_delete=models.PROTECT)
    image_image = models.FileField(default="image/default.jpg", upload_to="image/")
    notes = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = PostManager()

    class Meta(object):
        verbose_name = "Image"
        verbose_name_plural = "Images"
        ordering = ['equip_number']

    def __str__(self):
        return '%s - %s' % (self.equip_number, self.name)


    def get_absolute_url(self):
        return reverse_lazy('image-detail', args=[str(self.id)])