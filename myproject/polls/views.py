from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages

def login_register_view(request):
    if request.method == 'POST':
        action = request.POST.get('action')
        
        if action == 'login':
            username = request.POST.get('login')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                auth_login(request, user)
                return redirect('polls:index')
            else:
                messages.error(request, 'Nieprawidłowy login lub hasło.')

        
        elif action == 'register':
            username = request.POST.get('login')
            email = request.POST.get('email')
            pass1 = request.POST.get('password')
            pass2 = request.POST.get('password2')

            if pass1 != pass2:
                messages.error(request, 'Hasła nie są takie same.')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Ten login jest już zajęty.')
            else:
                User.objects.create_user(username=username, email=email, password=pass1)
                messages.success(request, 'Konto utworzone! Możesz się zalogować.')
                
    return render(request, 'polls/login.html')


def index(request):
    return render(request, 'polls/index.html')
def list_of_question(request):
    return render(request, 'polls/list_of_question.html')
