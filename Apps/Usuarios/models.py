from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager
from django.contrib.auth.models import User
from Apps.Market.models import Ship

# Create your models here.

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='avatares', blank=True, null=True)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    puntos = models.IntegerField(default=2500)
    naves = models.ManyToManyField(Ship, blank=True)

    def __str__(self):
        return self.user.username
    
    
