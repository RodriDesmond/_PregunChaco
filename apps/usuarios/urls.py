from django.urls import path
from .views import  *
from apps.usuarios import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'apps.usuarios'

urlpatterns = [
    path('registro/', views.registro.as_view(), name='registro'),
    path('login/', LoginView.as_view(template_name='usuarios/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='usuarios/logout.html'), name='logout'),
    #Perfil de usuario
    path('perfil/crear/',CrearPerfil.as_view(),name='crear_perfil'),
    path('<int:pk>/perfil/',VerPerfilView.as_view(),name='perfil'),
    path('<int:pk>/editar_perfil/', UserEditView.as_view(), name='editar_perfil'),
    
]
