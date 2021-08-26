from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = 'apps.resultado'

urlpatterns = [
    path('ranking',view_puntaje, name="ranking" ),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)