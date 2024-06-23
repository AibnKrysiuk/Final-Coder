from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import index, rank, about
from Apps.Usuarios.views import registro,login_view
from Apps.Market.views import market
from Apps.Juego.views import juego

urlpatterns = [
    path('', index, name='index'),
    path('juego', juego, name='juego'),
    path('rank', rank, name='rank'),
    path('about', about, name='about'),
    path('registro', registro, name='registro'),
    path('login', login_view, name='login'),
    path('logout', LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('market', market, name='market'),
]