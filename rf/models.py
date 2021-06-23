from django.db import models


class Product(models.Model):

    name = models.CharField(max_length=70, default='')
    description = models.CharField(max_length=255, default='')
    price = models.FloatField(default=0)