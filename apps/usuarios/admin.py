from django.contrib import admin
from .forms import UserRegisterForm

class MyModelAdmin(admin.ModelAdmin):
      form = UserRegisterForm
# Register your models here.