from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = 'apps.resultado'

urlpatterns = [
    path('puntaje',view_puntaje, name="puntaje"),
    path('api/pregunchaco/puntos',validar_puntos,name='Puntaje conseguido'),
    path('api/pregunchaco/scoreboard',scoreboard,name="scoreboard"),
    path('ranking',view_ranking, name="ranking" ),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)