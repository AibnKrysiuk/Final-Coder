from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import market, ship_formulario, comprar_nave
from Apps.Usuarios.views import registro,login_view, usuario
from Apps.Juego.views import juego

urlpatterns = [
    path('', market, name='market'),
    path('ship_formulario', ship_formulario, name='ship_formulario'),
    path('comprar_nave/<int:ship_id>/', comprar_nave, name='comprar_nave'),
    # path('usuario', usuario, name='usuario'),
    # path('juego', juego, name='juego'),
    # path('index', index, name='index'),
    # path('rank', rank, name='rank'),
    # path('about', about, name='about'),
    # path('login', login_view, name='login'),
    # path('logout', LogoutView.as_view(template_name="logout.html"), name='logout'),
    # path('registro', registro, name='registro'),
]