from apps.trivia.models import Categoria
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Puntaje(models.Model):
    categoria = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    puntaje = models.IntegerField()
