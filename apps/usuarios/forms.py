from django.forms.models import ModelForm
from apps.usuarios.models import Perfil
from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

#Redefine el formulario de registro
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)
    

    #Define los campos del Admin en usuarios y limpia el formulario de ayudas
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {k:"" for k in fields }

        def __init__(self, *args, **kwargs):
            super(UserRegisterForm,self).__init__(*args, **kwargs)

            self.fields['username'].widgets.attrs['class'] = 'form-control'
            self.fields['password1'].widgets.attrs['class'] = 'form-control'
            self.fields['password2'].widgets.attrs['class'] = 'form-control'


class CrearPerfil(ModelForm):
    first_name = forms.CharField(required=False,label="Nombre",widget=forms.TextInput)
    last_name = forms.CharField(required=False,label="Apellido",widget=forms.TextInput)
    imagen_perfil = forms.ImageField(required=False)
    facebook_url = forms.URLField(required=False)
    twitter_url = forms.URLField(required=False)
    instagram_url = forms.URLField(required=False)
    
    class Meta:
        model = Perfil
        fields = ['first_name','last_name','imagen_perfil','facebook_url','twitter_url','instagram_url']
