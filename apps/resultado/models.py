from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Puntaje(models.Model):
    categoria = models.CharField(max_length=20)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    puntaje = models.IntegerField()
    update = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} categoria {self.categoria}"


