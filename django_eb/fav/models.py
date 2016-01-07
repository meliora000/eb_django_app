
from django.db import models
from search.models import Object
from users.models import USER

# Create your models here.
class Favorite(models.Model):
    coffee = models.ForeignKey(Object)
    user = models.ForeignKey(USER)
    class Meta:
        unique_together = ('coffee','user')