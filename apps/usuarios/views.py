from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, UserManager
from django.urls.base import reverse
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from apps.usuarios.forms import CrearPerfil, UserRegisterForm
from django.shortcuts import get_object_or_404, render, HttpResponse, redirect, HttpResponseRedirect
from .models import *
from django.urls import reverse_lazy
from django.contrib import messages

class registro(CreateView):
        form_class = UserRegisterForm
        template_name = 'usuarios/registro.html'
        success_url = reverse_lazy('usuarios:login')
        

class UserEditView(UpdateView):
    model = Perfil
    template_name= 'usuarios/editar_perfil.html'    
    fields = ['email','username', 'first_name','last_name','imagen_perfil']
    success_url=reverse_lazy('trivia:home')   

class VerPerfilView(DetailView):
    model = Perfil
    template_name = 'usuarios/perfil.html'

    def get_context_data(self, *args, **kwargs):
        users = Perfil.objects.all()
        context = super(VerPerfilView, self).get_context_data(*args, **kwargs)
        
        user_pag = get_object_or_404(Perfil,id=self.kwargs['pk'])
        
        context["user_pag"] = user_pag
        return context

class CrearPerfil(CreateView):
        form_class = CrearPerfil
        template_name = 'usuarios/crear_perfil.html'
        success_url = reverse_lazy('trivia:home')

        def form_valid(self, form):
            perfil = form.save(commit=False)
            perfil.user = get_object_or_404(User,username=self.request.user)
            perfil.save()
            return HttpResponseRedirect(reverse('trivia:home'))

