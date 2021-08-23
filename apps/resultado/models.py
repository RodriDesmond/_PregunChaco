from django.db import models
from apps.trivia.models import Categoria
from django.contrib.auth.models import User

class Resultado(models.Model):
    trivia = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    puntaje = models.FloatField()

    def __str__(self):
        return str(self.id)
    
