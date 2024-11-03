from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length="30",verbose_name="name")
    cost = models.IntegerField(verbose_name="cost")