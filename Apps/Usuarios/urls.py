from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import registro,login_view,register,usuario,crear_avatar,administrar_post,listar_naves
from Apps.Pagina.views import borrar_post, post_formulario, actualizar_post
from Apps.Market.views import ship_formulario, borrar_nave, actualizar_nave
from django.urls import reverse_lazy

urlpatterns = [
    path('', login_view, name='login'),
    path('usuario', usuario, name='usuario'),
    path('logout', LogoutView.as_view(next_page=reverse_lazy('index')), name='logout'),
    path('register', register, name='register'),
    path('crear_avatar', crear_avatar, name='crear_avatar'),
    path('administrar_post', administrar_post, name='administrar_post'),
    path('borrar_post/<int:post_id>', borrar_post, name='borrar_post'),
    path('post_formulario', post_formulario, name='post_formulario'),
    path('actualizar_post/<int:post_id>', actualizar_post, name='actualizar_post'),
    path('listar_naves', listar_naves, name='listar_naves'),
    path('ship_formulario', ship_formulario, name='ship_formulario'),
    path('borrar_nave/<int:ship_id>', borrar_nave, name='borrar_nave'),
    path('actualizar_nave/<int:ship_id>', actualizar_nave, name='actualizar_nave'),

]