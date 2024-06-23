from django.shortcuts import render
from .forms import ShipFormulario
from .models import Ship

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