from django.db import models

# Create your models here.

class Object(models.Model):
    name = models.CharField(max_length=200)
    add = models.CharField(max_length=200)
    lat = models.FloatField()
    lng = models.FloatField()

class Obejct1(models.Model):
    name = models.CharField(max_length=200)