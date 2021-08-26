from apps.resultado.models import Puntaje
from django.shortcuts import render

# Create your views here.
def view_puntaje(request):
    user = request.user
    puntaje = Puntaje.objects.filter(user=user)
    context ={
        'puntaje' :puntaje
    }
    return render('puntaje', context)