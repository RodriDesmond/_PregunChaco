from django.urls import path
from .views import *

app_name = 'apps.trivia'

urlpatterns = [

    path('', home, name='home'),
    path('api/empezar-trivia/',empezar_trivia,name="empezar_trivia"),
    path('pregunchaco/',pregunchaco, name="pregunchaco"),
]