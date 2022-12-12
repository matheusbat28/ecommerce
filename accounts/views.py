from django.shortcuts import render, redirect
from validate_cpf import validate_cpf
from django.contrib import messages
from .models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib import auth

def Register(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name').strip().lower()
        last_name = request.POST.get('last_name').strip().lower()
        username = request.POST.get('username').strip().lower()
        telephone = request.POST.get('telephone').strip()
        cpf = request.POST.get('cpf').strip()
        email = request.POST.get('email').strip()
        password = request.POST.get('password').strip()
        password_2 = request.POST.get('password-2').strip()
        
        if not validate_cpf.is_valid(cpf):
            messages.error(request, 'CPF inválido')
            return redirect('register')
        if User.objects.filter(username = username).exists():
            messages.error(request, 'Usuário já existe')
            return redirect('register')
        if len(password) < 6:
            messages.error(request, 'Senha muito curta')
            return redirect('register')
        if password != password_2:
            messages.error(request, 'Senhas estão diferentes')
            return redirect('register')
        else:
            try:
                User.objects.create(
                    first_name = first_name,
                    last_name = last_name,
                    username = username,
                    telephone = telephone,
                    cpf = cpf,
                    email = email,
                    password = make_password(password)
                )
            except:
                messages.error(request, 'Erro ao cadastrar usuário')
            return redirect('login')
        
    else:
        return render(request, 'registration/index.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username').strip()
        password = request.POST.get('password').strip()
        valid_user = auth.authenticate(username=username, password=password)
        
        if valid_user is None:
            messages.error(request, 'Usuário não cadastrado')
            return redirect('login')
        elif valid_user is not None:
           auth.login(request, valid_user)
           return redirect('home')
        
    else:
        return render(request, 'login/index.html')
    

def home(request):
    return render(request, 'home/index.html')

def logout(request):
    auth.logout(request)
    return redirect('login')