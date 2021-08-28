from django.contrib import admin
from .forms import UserRegisterForm
from .models import Perfil

class MyModelAdmin(admin.ModelAdmin):
      form = UserRegisterForm
# Register your models here.

admin.site.register(Perfil)