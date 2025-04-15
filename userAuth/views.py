from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from userAuth.my_forms import LoginForm

# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login realizado com sucesso!")
            return redirect('meal:home')
        else:
            messages.success(request, "Usuário ou senha inválidos!")
            form = LoginForm()
            return render(request, 'login_user.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'login_user.html', {'form': form})
    
def logout_user(request):
    logout(request)
    messages.success(request, "Logout realizado com sucesso!")
    return redirect('userAuth:login_user')