import uuid
from django.db import models

class Restaurant(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rating = models.PositiveSmallIntegerField(blank=True)
    name = models.CharField(max_length=200, blank=True)
    site = models.URLField(blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=200, blank=True)
    street = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=200, blank=True)
    state = models.CharField(max_length=200, blank=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
