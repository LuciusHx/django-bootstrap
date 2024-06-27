from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.

#Pagina inicial

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'GET':

        return render(request, 'signup.html', {
            'form': UserCreationForm
            }
        )
    
    else:
        if request.POST['password1'] == request.POST['password2']:
            
            try:
                user = User.objects.create_user(username=request.POST['username'], password = request.POST('password1'))
                user.save()

                login(request, user)
                return redirect('home')
            
            except: 
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'Usuário já existe!'           
                               
                        }
                               
                   )

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Senhas são diferentes'

            }
        
        )