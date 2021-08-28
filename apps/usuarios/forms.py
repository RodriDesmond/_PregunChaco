from apps.usuarios.models import Perfil
from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
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


class EditProfileForm(UserChangeForm):
    email = forms.EmailField()
    imagen_perfil = forms.ImageField()
    username = forms.CharField(max_length=15, label='Nombre de usuario', widget=forms.TextInput(attrs={'class' : 'form.control'}))
    fist_name = forms.CharField(max_length=15,label='Nombre', widget=forms.TextInput(attrs={'class' : 'form.control'}))
    last_name = forms.CharField(label='Apellido', widget=forms.TextInput(attrs={'class' : 'form.control'})) 
    class Meta:
        model = Perfil
        fields = ['email','username', 'fist_name','last_name','imagen_perfil']
        help_texts = {k:"" for k in fields }