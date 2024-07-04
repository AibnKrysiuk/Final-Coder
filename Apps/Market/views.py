from django.shortcuts import render,redirect
from .forms import ShipFormulario
from .models import Ship
from Apps.Usuarios.views import usuario
from django.contrib.auth.decorators import user_passes_test, login_required
import os



# Create your views here.

# def market(req):
#     return render(req, "market.html")

def market(req):
    lista = Ship.objects.all()
    return render(req, 'market.html', {"market": lista})

def superuser_required(user):
    return user.is_superuser

@login_required
@user_passes_test(superuser_required)
def ship_formulario(req):

    if req.method == 'POST':
        miFormulario = ShipFormulario(req.POST, req.FILES)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data
            imagen = req.FILES.get('imagen')
            
            nuevo_ship = Ship(nombre=data['nombre'], descripcion=data['descripcion'], price=data['price'], imagen=imagen)
            nuevo_ship.save()

            lista = Ship.objects.all()

            return render(req, "market.html", {"market": lista})
        else:
            return render(req, "ship_formulario.html", {"message": "datos incorrectos"})
        
    else:
        miFormulario = ShipFormulario()
        return render(req, "ship_formulario.html", {"miFormulario": miFormulario})
    
@login_required(login_url='login')
def comprar_nave(req, ship_id):

    ship = Ship.objects.get(id=ship_id)
    

    profile = req.user.profile
    
    # Verificar si el usuario tiene suficientes puntos
    if profile.puntos >= ship.price:
        # Restar los puntos y guardar el perfil
        profile.puntos -= ship.price
        profile.save()
        
        # Asignar la nave al usuario
        profile.naves.add(ship)
        
        # Redirigir a alguna página de éxito
        lista = Ship.objects.all()
        return render(req, "market.html", {"market": lista})
    else:
        # Redirigir a alguna página de error
        lista = Ship.objects.all()
        return render(req, "market.html", {"market": lista})
    
def borrar_nave(req, ship_id):
    nave_a_borrar = Ship.objects.get(id=ship_id)
    nave_a_borrar.delete()

    naves = Ship.objects.all().order_by('-id')
    return render(req, "market.html", {"market": naves})

def actualizar_nave(req, ship_id):
    nave_a_actualizar = Ship.objects.get(id=ship_id)

    if req.method == 'POST':
        imagen_anterior = nave_a_actualizar.imagen.path if nave_a_actualizar.imagen else None
        mi_formulario = ShipFormulario(req.POST, req.FILES, instance=nave_a_actualizar)

        if mi_formulario.is_valid():
            if 'imagen' in req.FILES and imagen_anterior:
                if os.path.isfile(imagen_anterior):
                    os.remove(imagen_anterior)

            mi_formulario.save()
            naves = Ship.objects.all().order_by('-id')
            return render(req, "market.html", {"market": naves})
    else:
        mi_formulario = ShipFormulario(instance=nave_a_actualizar)
    return render(req, "actualizar_nave.html", {"miFormulario": mi_formulario, 'ship': nave_a_actualizar})
