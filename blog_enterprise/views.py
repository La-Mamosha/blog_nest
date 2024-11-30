from django.http import HttpResponse
from django.shortcuts import render, redirect

from blogs.models import Category, Blog
from .forms import RegistrationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.models import Group


##########################################################################################################################
def home(request):
    posts = Blog.objects.filter(is_featured=True).order_by('-created_at') # Si es false no lo devuelve
    context = {
        'posts': posts
    }
    
    return render(request, 'home.html', context) 

##########################################################################################################################
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST) #Viene con los datos tipiado
        if form.is_valid():
            user =form.save()
            group = Group.objects.get(name='grupo_permiso')
            group.user_set.add(user)
            
            return redirect('register')
    else:
        form = RegistrationForm()
    
    form = RegistrationForm()
    context =  {
        'form': form
    }
    return render(request, 'register.html', context)

##########################################################################################################################
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            #Capturando los datos del formulario
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            #Realizando la validación del usuario y contraseña
            user = auth.authenticate(username=username, password=password)
            if user is not None: # Si jusuario no es nulo o en blanco
                auth.login(request, user) #user= Objeto que va a iniciar sesión, Request=Inicio de sesión
                return redirect('home') # Redireccionando am la pagina principal
    
    form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)

##########################################################################################################################
def logout(request):
    auth.logout(request)
    return redirect('home')
