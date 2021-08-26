from django.http.response import JsonResponse
from apps.preguntas.models import Pregunta
import json
from apps.trivia.models import Categoria
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
    id = data.get('id')
    soluciones = json.loads(data.get('data'))
    categoria = Categoria.objects.get(id=id)
    puntaje = 0
    for solucion in soluciones:
        pregunta = Pregunta.objects.filter(id = solucion.get('pregunta_id')).first()
        if (pregunta.respuestas.respuesta) == solucion.get('respuesta'):
            if(pregunta.respuestas.respuesta.correcta):
                puntaje = puntaje + pregunta.puntos
   
    puntaje_total = Puntaje(categoria = categoria , puntaje = puntaje  , user = user)
    puntaje_total.save() 
    
    return JsonResponse({'message' : 'success' , 'status':True})