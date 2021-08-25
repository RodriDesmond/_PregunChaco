from django.urls import path
from .views import  *

app_name = 'apps.usuarios'

urlpatterns = [
    path('login', login_attempt, name="login_attempt" ),
    path('register', register_attempt, name="register_attempt" )
]
