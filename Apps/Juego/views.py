from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Apps.Usuarios.models import Avatar
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

@login_required(login_url='login')
def juego(req):
    try:
        avatar = Avatar.objects.get(user=req.user)
        url_avatar = avatar.imagen.url
    except ObjectDoesNotExist:
        url_avatar = None
    return render(req, "juego.html", {"url": url_avatar})