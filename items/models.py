from django.db import models

# Create your models here.
from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    inventory = models.IntegerField()
    image_url = models.CharField(max_length=2100)


class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=30)
    discount = models.FloatField()
