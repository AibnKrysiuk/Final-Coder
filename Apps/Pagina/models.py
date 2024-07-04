from django.db import models
import os
# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    fecha = models.DateField()
    meGusta = models.IntegerField()
    imagen = models.ImageField(upload_to='post', blank=True, null=True)
    texto = models.TextField(default='No hay texto para mostrar')

    def __str__(self):
        return f'{self.titulo} - {self.autor} - {self.fecha} - {self.meGusta} - {self.imagen} - {self.texto}'
    
    def delete(self, *args, **kwargs):
        if self.imagen and os.path.isfile(self.imagen.path):
            os.remove(self.imagen.path)
        super().delete(*args, **kwargs)
