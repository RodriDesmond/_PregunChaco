from django.forms.forms import Form
from django.shortcuts import render

'''
def login_attempt(request):
    return render(request,'auth/login.html')

def register_attempt(request):
    return render(request,'auth/register.html')'''

from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import UserRegisterForm
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado correctamente')
    else:
        form = UserRegisterForm()    

    context = { 'form' : form }
    return render(request, 'registroTest.html', context)