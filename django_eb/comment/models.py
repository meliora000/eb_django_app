from __future__ import unicode_literals

from django.db import models
from search.models import Object
from users.models import USER
from django.utils import timezone

# Create your models here.

class Comment(models.Model):
    coffee = models.ForeignKey(Object)
    user = models.ForeignKey(USER)
    taste = models.BooleanField(default=False)
    mood = models.BooleanField(default=False)
    price = models.BooleanField(default=False)
    comment = models.CharField(max_length=120,null=True)

    class Meta:
        unique_together = ('coffee','user')

class Commenta(models.Model):
    coffee = models.ForeignKey(Object)
    user = models.ForeignKey(USER)
    rate = models.IntegerField()
    comment = models.CharField(max_length=500,null=True)
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        unique_together = ('coffee','user')

class Hashtag(models.Model):
    name = models.CharField(null=False,unique=True,max_length=100)
    coffeeid = models.CharField(null=False,max_length=5000)
