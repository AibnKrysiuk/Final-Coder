from django.shortcuts import render
from Apps.Juego.views import juego
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.core.exceptions import ObjectDoesNotExist
from .models import Avatar
from .forms import AvatarForm

# Create your views here.

def registro(req):
    return render(req, "registro.html")


@login_required
def usuario(req):
    try:
        avatar = Avatar.objects.get(user=req.user)
        url_avatar = avatar.imagen.url
    except ObjectDoesNotExist:
        url_avatar = None

    return render(req, "usuario.html", {"url": url_avatar})

# def usuario(req):
#     usuario = req.user
#     avatar = usuario.avatar
#     naves = usuario.naves.all()

#     return render(req, "usuario.html", {"url": avatar.imagen.url, "naves": naves})

def login_view(req):
    if req.method == 'POST':
        miFormulario = CustomAuthenticationForm(req, data=req.POST)

        if miFormulario.is_valid():
            data = miFormulario.cleaned_data

            usuario = data["username"]
            psw = data["password"]

            user = authenticate(username=usuario, password=psw)

            if user:
                login(req, user)
                return render(req, "juego.html" , {"message": f'Bienvenido {usuario}'})
            else:
                return render(req, "login.html" , {"miFormulario": miFormulario, "message": 'Datos incorrectos'})
        else:
            return render(req, "login.html" , {"miFormulario": miFormulario, "message": 'Datos incorrectos'})
        
    else: 
        miFormulario = CustomAuthenticationForm()
        return render(req, "login.html", {"miFormulario": miFormulario})
    
def register(req):
    if req.method == 'POST':
        miFormulario = CustomUserCreationForm(req.POST)

        if miFormulario.is_valid():
            miFormulario.save()

            miFormulario2 = CustomAuthenticationForm(req, data=req.POST)
            return render(req, "login.html", {"miFormulario": miFormulario2})
        else:
            return render(req, "registro.html", {"miFormulario": miFormulario, "message": 'Datos incorrectos'})
        
    else: 
        miFormulario = CustomUserCreationForm()
        return render(req, "registro.html", {"miFormulario": miFormulario})
    
@login_required
def crear_avatar(req):
    if req.method == 'POST':
        form = AvatarForm(req.POST, req.FILES)
        if form.is_valid():
            avatar = form.save(commit=False)
            avatar.user = req.user
            avatar.save()

            try:
                avatar = Avatar.objects.get(user=req.user)
                url_avatar = avatar.imagen.url
            except ObjectDoesNotExist:
                url_avatar = None

            return render(req, "usuario.html", {"url": url_avatar})
            # return render(req, "usuario.html")  # Redirigir a la vista de usuario
    else:
        form = AvatarForm()
    return render(req, 'crear_avatar.html', {'form': form})