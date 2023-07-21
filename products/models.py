from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=50)
    users = models.ManyToManyField('auth.user', related_name='products')
