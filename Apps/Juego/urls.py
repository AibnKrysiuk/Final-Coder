from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import juego
from Apps.Pagina.views import index, rank, about
from Apps.Usuarios.views import registro,login_view
from Apps.Market.views import market, ship_formulario

urlpatterns = [
    path('', juego, name='juego'),
    # path('index', index, name='index'),
    # path('rank', rank, name='rank'),
    # path('about', about, name='about'),
    # path('login', login_view, name='login'),
    # path('logout', LogoutView.as_view(template_name="logout.html"), name='logout'),
    # path('registro', registro, name='registro'),
    # path('market', market, name='market'),
    path('ship_formulario', ship_formulario, name='ship_formulario'),
]