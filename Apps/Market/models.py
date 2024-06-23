from django.db import models

# Create your models here.

class Ship(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField(default="Sin descripcion")
    price = models.IntegerField()
    imagen = models.ImageField(upload_to='market', blank=True, null=True)

    def __str__(self):
        return f'{self.nombre} - {self.descripcion} - {self.price}'