from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = 'apps.trivia'

urlpatterns = [
    path('', home, name='home'),
    path('categorias', elegir_categorias, name='categorias'),
    path('api/pregunchaco/',empezar_pregunchaco,name="api_preguntas"),
    path('pregunchaco/',pregunchaco, name="pregunchaco"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)