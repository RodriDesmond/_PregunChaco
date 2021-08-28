from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from apps.usuarios.forms import UserRegisterForm, EditProfileForm
from django.shortcuts import get_object_or_404, render, HttpResponse, redirect, HttpResponseRedirect
from .models import *
from django.urls import reverse_lazy
from django.contrib import messages

def registro(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado correctamente')
            return redirect('/login/')
    else:
        form = UserRegisterForm()    

    context = { 'form' : form }
    return render(request, 'usuarios/registro.html', context)

class UserEditView(UpdateView):
    model = Perfil
    form_class= EditProfileForm
    template_name= 'usuarios/editar_perfil.html'
    success_url=reverse_lazy('trivia:home')

    def get_object(self):
        return self.request.user

class VerPerfilView(DetailView):
    model = Perfil
    template_name = 'usuarios/perfil.html'

    def get_context_data(self, *args, **kwargs):
        users = Perfil.objects.all()
        context = super(VerPerfilView, self).get_context_data(*args, **kwargs)
        
        user_pag = get_object_or_404(Perfil,id=self.kwargs['pk'])
        
        context["user_pag"] = user_pag
        return context


