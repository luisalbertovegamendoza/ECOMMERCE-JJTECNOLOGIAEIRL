from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def registro_usuario(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']

        if User.objects.filter(username=username).exists():
            messages.error(request, "El usuario ya existe")
            return redirect('registro')

        User.objects.create_user(username=username , password=password)
        messages.success(request, "Usuario registrado exitosamente")
        return redirect('login')

    return render(request, 'usuarios/registro.html')

def login_usuario(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "Usuario o contraseña incorrectos")
            return redirect('login')

    return render(request,'usuarios/login.html')

def logout_usuario(request):
    logout(request)
    return redirect('index')
