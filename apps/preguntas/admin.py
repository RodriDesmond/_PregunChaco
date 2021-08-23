from django.contrib import admin
from .models import Pregunta, Respuesta

class RespuestaAdministrador(admin.StackedInline):
    model = Respuesta

class PreguntaAdmin(admin.ModelAdmin):
    inlines = [RespuestaAdministrador]

admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Respuesta)
