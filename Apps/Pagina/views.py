from django.shortcuts import render
from .models import Post
from Apps.Usuarios.models import Avatar, Puntos
from .forms import PostFormulario

# Create your views here.


def index(req):

    avatar = Avatar.objects.get(user=req.user.id)
    try:
        puntos = Puntos.objects.get(user=req.user.id)
    except Puntos.DoesNotExist:
        puntos = Puntos.objects.create(user=req.user, puntos=100)

    lista = Post.objects.all()
    return render(req, "index.html", {"url": avatar.imagen.url, "lista_post": lista , "puntos": puntos})

def rank(req):
    return render(req, "rank.html")

def about(req):
    return render(req, "about.html")

def post_formulario(req):

    if req.method == 'POST':
        miFormulario = PostFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            nuevo_post = Post(titulo=data['titulo'], autor=['autor'], fecha=['fecha'], meGusta=['meGusta'], texto={'texto'})
            nuevo_post.save()

            lista = Post.objects.all()

            return render(req, "index.html", {"index": lista})
        else:
            return render(req, "index.html", {"message": "datos incorrectos"})
        
    else:
        # miFormulario = ShipFormulario()
        return render(req, "index.html")