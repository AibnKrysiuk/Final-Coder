from django.shortcuts import render
from Apps.Juego.views import juego
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from .models import Avatar, Naves

# Create your views here.

def registro(req):
    return render(req, "registro.html")

def usuario(req):
    avatar = Avatar.objects.get(user=req.user.id)
    naves = Naves.objects.filter(user=req.user.id)

    return render(req, "usuario.html", {"url": avatar.imagen.url, "naves": naves})

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
            usuario = miFormulario.cleaned_data.get('username')
            return render(req, "juego.html" , {"message": f'Usuario:  {usuario} creado con éxito'})
        else:
            return render(req, "registro.html", {"miFormulario": miFormulario, "message": 'Datos incorrectos'})
        
    else: 
        miFormulario = CustomUserCreationForm()
        return render(req, "registro.html", {"miFormulario": miFormulario})