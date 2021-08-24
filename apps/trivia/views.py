from django.http.response import Http404, HttpResponse, JsonResponse
from .models import *
from apps.preguntas.models import *
import random
from django.shortcuts import redirect, render


def home(request):
    context = {
        'categorias': Categoria.objects.all()
    }
    if request.GET.get('categoria'):
        return redirect(f"/pregunchaco/?categoria={request.GET.get('categoria')}")
    return render(request, 'home.html', context)


def pregunchaco(request):
    context = {
        'categoria': request.GET.get('categoria')
    }
    return render(request, 'pregunchaco.html', context)


def empezar_pregunchaco(request):
    try:
        pregunta_objs = Pregunta.objects.all()

        if request.GET.get('categoria'):
            pregunta_objs = pregunta_objs.filter(
                categoria__nombre_categoria__icontains=request.GET.get('categoria')
            )

        pregunta_objs = list(pregunta_objs)
        data = []
        for pregunta_obj in pregunta_objs:
            data.append({
                "id": pregunta_obj.id,
                "categoria": pregunta_obj.categoria.nombre_categoria,
                "logo_categoria":pregunta_obj.categoria.logo_url(),
                "pregunta_enunciado": pregunta_obj.pregunta_enunciado,
                "dato": pregunta_obj.dato,
                "puntos": pregunta_obj.puntos,
                "respuestas": pregunta_obj.obtener_respuesta(),
                "imagen" : pregunta_obj.imagen_url(),
            })

        payload = {'status': True, 'data': data}
        return JsonResponse(payload)

    except Exception as e:
        print(e)
    return HttpResponse("Algo malio sal")