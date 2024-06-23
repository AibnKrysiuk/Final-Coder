from django.shortcuts import render
from .models import Post
from .forms import PostFormulario
from Apps.Usuarios.models import Profile
from django.contrib.auth.models import User
from Apps.Usuarios.models import Avatar
import datetime

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

# def rank(req):
#     return render(req, "rank.html")

def about(req):
    return render(req, "about.html")


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
    
def rank(req):
    perfiles = Profile.objects.order_by('-puntos')[:10] 
    usuarios_con_puntos = [{'username': perfil.user.username, 'puntos': perfil.puntos} for perfil in perfiles]
    

    while len(usuarios_con_puntos) < 10:
        usuarios_con_puntos.append({'username': 'Vacante', 'puntos': 0})
    

    for idx, usuario in enumerate(usuarios_con_puntos):
        usuario['posicion'] = idx + 1
    
    return render(req, 'rank.html', {'usuarios_con_puntos': usuarios_con_puntos})