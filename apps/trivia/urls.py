from django.urls import path
from .views import *

app_name = 'apps.trivia'

urlpatterns = [

    path('', home, name='home'),
    path('api/',empezar_pregunchaco,name="api_preguntas"),
    path('pregunchaco/',pregunchaco, name="pregunchaco"),
]