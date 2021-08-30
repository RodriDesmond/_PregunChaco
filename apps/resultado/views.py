from django.contrib.auth.models import User
from apps.trivia.models import Categoria
from django.http import request
from django.http.response import HttpResponse, JsonResponse
from django.urls.base import reverse_lazy
from apps.preguntas.models import Pregunta
import json
from apps.resultado.models import Puntaje
from django.shortcuts import  render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='/login')
def view_puntaje(request,pk):
    user = User.objects.get(pk=pk)
    puntaje = Puntaje.objects.filter(user=user)
    context ={
        'puntaje' :puntaje,
        'user':user
    }
    return render(request,'puntajes/puntaje.html', context)

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


def scoreboard(request):
    try:
        puntajes = Puntaje.objects.all()
        puntajes = list(puntajes)
        data = []
        for p in puntajes:
            data.append({
                'categoria': p.categoria,
                'user' : p.user.username,
                'puntaje' : p.puntaje,
                'fecha' : p.update,
            })

        payload = {'status': True, 'data': data}
        return JsonResponse(payload)

    except Exception as e:
        print(e)
    return HttpResponse("Algo malio sal")


def view_ranking(request):

    context = {
        'categoria': request.GET.get('categoria'),
        'user_id' : request.GET.get('user_id'),
        'puntaje' : request.GET.get('puntaje'),
        'fecha' : request.GET.get('fecha'),
    }
    return render(request,'puntajes/ranking.html', context)