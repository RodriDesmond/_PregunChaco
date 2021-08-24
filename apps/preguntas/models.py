from PregunChaco.settings.local import MEDIA_ROOT
from django.db import models
from apps.trivia.models import BaseModel, Categoria
from django.core.files.storage import FileSystemStorage
import random

# Create your models here.
fs = FileSystemStorage(location=MEDIA_ROOT)

class Pregunta(BaseModel):
    categoria = models.ForeignKey(Categoria, related_name='categoria', on_delete=models.CASCADE)
    pregunta_enunciado = models.TextField(max_length=100)
    dato = models.TextField(max_length=600)
    puntos = models.PositiveIntegerField(default=5)
    imagen = models.ImageField(storage = fs )

    def __str__(self):
        return self.pregunta_enunciado
    
    def imagen_url(self):
        if self.imagen and hasattr(self.imagen, 'url'):
            return self.imagen.url

    def obtener_respuesta(self):
        respuesta_objs = list(Respuesta.objects.filter(pregunta = self))
        random.shuffle(respuesta_objs)    
        respuestas = []
        for respuesta_obj in respuesta_objs:
            respuestas.append({
                'respuesta': respuesta_obj.respuesta_enunciado,
                'correcta': respuesta_obj.correcta,
            })
        return respuestas

class Respuesta(BaseModel):
    pregunta = models.ForeignKey(Pregunta, related_name='pregunta',on_delete=models.CASCADE)
    respuesta_enunciado = models.CharField(max_length=100)
    correcta = models.BooleanField(default=False)

    def __str__(self):
        return self.respuesta_enunciado
