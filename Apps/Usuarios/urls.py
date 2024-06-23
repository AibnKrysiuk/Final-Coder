from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import registro,login_view,register,usuario,crear_avatar
from django.urls import reverse_lazy

urlpatterns = [
    path('', login_view, name='login'),
    path('usuario', usuario, name='usuario'),
    path('logout', LogoutView.as_view(next_page=reverse_lazy('index')), name='logout'),
    path('register', register, name='register'),
    path('crear_avatar', crear_avatar, name='crear_avatar'),
    # path('juego', juego, name='juego'),
    # path('index', index, name='index'),
    # path('rank', rank, name='rank'),
    # path('about', about, name='about'),
    # path('market', market, name='market'),
]