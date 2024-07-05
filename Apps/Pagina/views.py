from django.shortcuts import render
from .models import Post
from .forms import PostFormulario
from Apps.Usuarios.models import Profile
from django.contrib.auth.models import User
from Apps.Usuarios.models import Avatar
from django.core.exceptions import ObjectDoesNotExist
import datetime
import os

# Create your views here.


def index(req):
    avatar_url = None
    if req.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(user=req.user.id)
            avatar_url = avatar.imagen.url
        except Avatar.DoesNotExist:
            pass  
    lista = Post.objects.all().order_by('-id')
    return render(req, "index.html", {"url": avatar_url, "lista_post": lista})


def about(req):
    try:
        avatar = Avatar.objects.get(user=req.user)
        url_avatar = avatar.imagen.url
    except ObjectDoesNotExist:
        url_avatar = None

    return render(req, "about.html", {"url": url_avatar})



def post_formulario(req):

    if req.method == 'POST':
        miFormulario = PostFormulario(req.POST, req.FILES)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            imagen = req.FILES.get('imagen')

            nuevo_post = Post(titulo=data['titulo'], autor=data['autor'], fecha=data['fecha'], meGusta=data['meGusta'], imagen=imagen,texto=data['texto'])
            nuevo_post.save()

            lista = Post.objects.all().order_by('-id')

            return render(req, "index.html", {"lista_post": lista})
        else:
            return render(req, "index.html", {"message": "datos incorrectos"})
        
    else:
        miFormulario = PostFormulario()
        return render(req, "post_formulario.html", {"miFormulario": miFormulario})
    
def borrar_post(req, post_id):
    post_por_borrar = Post.objects.get(id=post_id)
    post_por_borrar.delete()

    lista = Post.objects.all().order_by('-id')
    return render(req, "index.html", {"lista_post": lista})

def actualizar_post(req, post_id):
    post_a_actualizar = Post.objects.get(id=post_id)

    if req.method == 'POST':

        imagen_anterior = post_a_actualizar.imagen.path if post_a_actualizar.imagen else None

        mi_formulario = PostFormulario(req.POST, req.FILES, instance=post_a_actualizar)

        if mi_formulario.is_valid():
            if 'imagen' in req.FILES and imagen_anterior:
                if os.path.isfile(imagen_anterior):
                    os.remove(imagen_anterior)

            mi_formulario.save()
            lista = Post.objects.all().order_by('-id')
            return render(req, "index.html", {"lista_post": lista})
    else:
        mi_formulario = PostFormulario(instance=post_a_actualizar)
    
    return render(req, "actualizar_post.html", {"miFormulario": mi_formulario, 'post': post_a_actualizar})


def rank(req):
    try:
        avatar = Avatar.objects.get(user=req.user)
        url_avatar = avatar.imagen.url
    except ObjectDoesNotExist:
        url_avatar = None

    perfiles = Profile.objects.order_by('-puntos')[:10] 
    usuarios_con_puntos = [{'username': perfil.user.username, 'puntos': perfil.puntos} for perfil in perfiles]
    

    while len(usuarios_con_puntos) < 10:
        usuarios_con_puntos.append({'username': 'Vacante', 'puntos': 0})
    

    for idx, usuario in enumerate(usuarios_con_puntos):
        usuario['posicion'] = idx + 1
    
    return render(req, 'rank.html', {'usuarios_con_puntos': usuarios_con_puntos, "url": url_avatar})