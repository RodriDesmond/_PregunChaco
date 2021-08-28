from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Perfil(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    imagen_perfil = models.ImageField(null=True, blank=True, upload_to="perfil/")
    facebook_url = models.TextField(max_length=250, null=True, blank=True)
    twitter_url = models.TextField(max_length=250, null=True, blank=True)
    instagram_url = models.TextField(max_length=250, null=True, blank=True)

    def __str__(self):
        return str(self.user)