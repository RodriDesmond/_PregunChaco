from django.http.response import JsonResponse
from apps.preguntas.models import Pregunta, Respuesta
import json
from apps.resultado.models import Puntaje
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login')
def view_puntaje(request):
    user = request.user
    puntaje = Puntaje.objects.filter(user=user)
    context ={
        'puntaje' :puntaje
    }
    return render(request,'puntaje.html', context)

@csrf_exempt
@login_required(login_url='/login')
def validar_puntos(request):
    data = json.loads(request.body)
    user = request.user    
    soluciones = json.loads(data.get('data'))
    categoria = soluciones[0].get('categoria')    
    puntaje = 0

    
    for solucion in soluciones:
        pregunta = Pregunta.objects.filter(id = solucion.get('pregunta_id')).first()
        if solucion.get('correcto'):
            puntaje = puntaje + pregunta.puntos

   
    puntaje_total = Puntaje(categoria = categoria , puntaje = puntaje  , user = user)
    puntaje_total.save() 
    
    return JsonResponse({'message' : 'puntos cargados' , 'status':True})
