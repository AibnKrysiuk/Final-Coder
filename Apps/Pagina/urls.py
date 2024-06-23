from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import index, rank, about, post_formulario

# from Apps.Market.views import market
# from Apps.Juego.views import juego

urlpatterns = [
    path('', index, name='index'),
    # path('juego', juego, name='juego'),
    path('rank', rank, name='rank'),
    path('about', about, name='about'),
    path('post_formulario', post_formulario, name='post_formulario'),
    # path('registro', registro, name='registro'),
    # path('login', login_view, name='login'),
    # path('usuario', usuario, name='usuario'),
    # path('logout', LogoutView.as_view(template_name="index.html"), name='logout'),
    # # path('market', market, name='market'),
]