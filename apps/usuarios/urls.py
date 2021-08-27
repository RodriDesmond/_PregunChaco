from django.urls import path
from .views import  *
from django.contrib.auth import views as auth_views
from apps.usuarios import views
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'apps.usuarios'

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', LoginView.as_view(template_name='loginTest.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='logout.html'), name='logout'),
]
