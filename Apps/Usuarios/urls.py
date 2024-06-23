from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import registro,login_view,register,usuario
from Apps.Pagina.views import index, rank, about
from Apps.Market.views import market
from Apps.Juego.views import juego

urlpatterns = [
    path('', login_view, name='login'),
    path('usuario', usuario, name='usuario'),
    path('logout', LogoutView.as_view(template_name="logout.html"), name='logout'),
    path('register', register, name='register'),
    path('juego', juego, name='juego'),
    path('index', index, name='index'),
    path('rank', rank, name='rank'),
    path('about', about, name='about'),
    path('market', market, name='market'),
]