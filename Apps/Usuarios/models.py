from django.db import models
from django.contrib.auth.models import User
from Apps.Market.models import Ship

# Create your models here.

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)

class Puntos(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    puntos = models.IntegerField(default= 100)

class Naves(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    naves = models.ForeignKey(Ship, on_delete=models.CASCADE)
