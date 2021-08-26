from apps.trivia.models import Categoria
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Puntaje(models.Model):
    trivia = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()