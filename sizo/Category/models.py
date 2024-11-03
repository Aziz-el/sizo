from django.db import models
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=40)
    description = models.TextField(max_length=256)