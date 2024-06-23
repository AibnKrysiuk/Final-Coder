from django.shortcuts import render,redirect
from .forms import ShipFormulario
from .models import Ship
from Apps.Usuarios.views import usuario
from django.contrib.auth.decorators import user_passes_test, login_required



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
    # Obtener la nave seleccionada
    ship = Ship.objects.get(id=ship_id)
    
    # Obtener el perfil del usuario logueado
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
    
# def comprar_nave(req):
#     if req.method == 'POST':
#         nave_id = req.POST.get('nave_id')
#         nave = Ship.objects.get(pk=nave_id)
#         usuario = req.user
        
#         if usuario.puntos >= nave.price:
#             # Restar los puntos necesarios para comprar la nave
#             usuario.puntos -= nave.price
#             usuario.save()
            
#             # Agregar la nave al usuario
#             usuario.nave = nave
#             usuario.save()
            
#             lista = Ship.objects.all()
#             return render(req, 'market.html', {"market": lista})  # Redirigir a la página principal después de comprar la nave
#         else:
#             lista = Ship.objects.all()
#             return render(req, 'market.html', {"market": lista, "message": "No tienes suficientes puntos"})  # Mostrar un mensaje de que no tienes suficientes puntos
#     else:
#         # Lógica para mostrar las naves disponibles para comprar en un formulario
#         lista = Ship.objects.all()
#         return render(req, 'market.html', {"market": lista})

# def ship_formulario(req):

#     if req.method == 'POST':
#         miFormulario = ShipFormulario(req.POST, req.FILES)

#         if miFormulario.is_valid():

#             data = miFormulario.cleaned_data

#             nuevo_ship = Ship(nombre=data['nombre'], price=data['price'], descripcion=['descripcion'], imagen=['imagen'])
#             nuevo_ship.save()

#             lista = Ship.objects.all()

#             return render(req, "market.html", {"market": lista})
#         else:
#             return render(req, "ship_formulario.html", {"message": "datos incorrectos"})
        
#     else:
#         miFormulario = ShipFormulario()
#         return render(req, "ship_formulario.html", {"miFormulario": miFormulario})