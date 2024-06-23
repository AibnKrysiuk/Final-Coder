from django.shortcuts import render
from .models import Post
from .forms import PostFormulario
from Apps.Usuarios.models import Avatar

# Create your views here.


def index(req):
    avatar_url = None
    if req.user.is_authenticated:
        try:
            avatar = Avatar.objects.get(user=req.user.id)
            avatar_url = avatar.imagen.url
        except Avatar.DoesNotExist:
            pass  
    lista = Post.objects.all()
    return render(req, "index.html", {"url": avatar_url, "lista_post": lista})

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