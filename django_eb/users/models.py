from django.db import models

class USER(models.Model):
    name = models.CharField(max_length=200)
    userid = models.CharField(max_length=200,primary_key=True)
    userpassword = models.CharField(max_length=200)
    add = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=30,null=False)