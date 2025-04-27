from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation
from versatileimagefield.fields import VersatileImageField, PPOIField


# Create your models here.
class Photo(models.Model):
    photo_id = models.UUIDField()
    user_ip = models.GenericIPAddressField()
    uploaded_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now=True)
    note = models.TextField(max_length=100)
    origin_image = VersatileImageField(
        upload_to="origin_images", ppoi_field="ppoi", null=True, blank=True
    )
    generated_image = VersatileImageField(
        upload_to="generated_images", ppoi_field="ppoi", null=True, blank=True
    )
    ppoi = PPOIField(null=True, blank=True)

    def __str__(self):
        return self.photo_id
