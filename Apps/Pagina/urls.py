from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import index, rank, about, post_formulario, actualizar_post

# from Apps.Market.views import market
# from Apps.Juego.views import juego

urlpatterns = [
    path('', index, name='index'),
    path('rank', rank, name='rank'),
    path('about', about, name='about'),
    path('post_formulario', post_formulario, name='post_formulario'),
]