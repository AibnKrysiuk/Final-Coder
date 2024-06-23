from django.contrib import admin
from .models import Post
from Apps.Usuarios.models import Puntos

# Register your models here.
admin.site.register(Post)
admin.site.register(Puntos)