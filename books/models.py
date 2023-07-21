from django.db import models

class Book(models.Model):
    user = models.ForeignKey('auth.User', related_name='books', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
