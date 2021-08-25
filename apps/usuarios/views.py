from django.shortcuts import render


def login_attempt(request):
    return render(request,'auth/login.html')

def register_attempt(request):
    return render(request,'auth/register.html')