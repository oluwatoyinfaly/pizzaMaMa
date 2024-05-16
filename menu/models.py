'''Pizza menu models'''
from django.db import models

# Create your models here.
class Pizza(models.Model):
    '''Pizza model'''
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    ingredients = models.CharField(max_length=400)
    vegetarian = models.BooleanField(default=False)

    def __str__(self):
        return self.name
