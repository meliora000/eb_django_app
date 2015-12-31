from __future__ import unicode_literals

from django.db import models
from search.models import Object
from users.models import USER
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

