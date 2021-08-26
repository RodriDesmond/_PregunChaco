from apps.trivia.models import Categoria
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Puntaje(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    puntaje = models.IntegerField()

    def __str__(self):
        return self.user.username