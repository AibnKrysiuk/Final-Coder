from django.shortcuts import render,redirect
from .forms import ShipFormulario
from .models import Ship
from Apps.Usuarios.models import Puntos

# Create your views here.

# def market(req):
#     return render(req, "market.html")

def market(req):
    lista = Ship.objects.all()
    return render(req, 'market.html', {"market": lista})

def ship_formulario(req):

    if req.method == 'POST':
        miFormulario = ShipFormulario(req.POST)

        if miFormulario.is_valid():

            data = miFormulario.cleaned_data

            nuevo_ship = Ship(nombre=data['nombre'], descripcion=data['descripcion'], price=data['price'])
            nuevo_ship.save()

            lista = Ship.objects.all()

            return render(req, "market.html", {"market": lista})
        else:
            return render(req, "ship_formulario.html", {"message": "datos incorrectos"})
        
    else:
        miFormulario = ShipFormulario()
        return render(req, "ship_formulario.html", {"miFormulario": miFormulario})
    
def comprar_nave(req):
    if req.method == 'POST':
        nave_id = req.POST.get('nave_id')
        nave = Ship.objects.get(pk=nave_id)
        puntos = Puntos.objects.get(user=req.user)
        
        if puntos.puntos >= nave.precio:
            # Restar los puntos necesarios para comprar la nave
            puntos.puntos -= nave.precio
            puntos.save()
            
            # Agregar la nave al usuario (aquí asumimos que tienes un modelo de Usuario)
            usuario = req.user
            usuario.nave = nave
            usuario.save()
            
            return redirect('usuario.html')  # Redirigir a la página principal después de comprar la nave
        else:
            return render(req, 'market.html')  # Mostrar un mensaje de que no tienes suficientes puntos
    else:
        # Lógica para mostrar las naves disponibles para comprar en un formulario
        nave = Ship.objects.all()
        return render(req, 'market.html', {'naves': nave})

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