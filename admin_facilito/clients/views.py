from django.shortcuts import render, redirect
from django.http import HttpResponse
from forms import LoginForm
from django.contrib.auth import authenticate, login as login_django, logout as logout_django

# Create your views here.
def show(request):
    return HttpResponse("Prueba correcta")


def login(request):
    # Si nos estan enviando el formulario .:.
    message = None
    if request.method == 'POST':
        username_post = request.POST['username']
        password_post = request.POST['password']
        
        # Se verifica si el usuario y contasena mandado existen dentro de la base de datos.
        user = authenticate(username=username_post, password=password_post)
        if user is not None:
            login_django(request, user)
            return redirect('client:dashboard')
        else:
            message = "Username o password incorrectos"

    form = LoginForm()
    context = {
        'form': form,
        'message': message
    }
    return render(request, 'login.html', context)

def logout(request):
    logout_django(request)
    return redirect('client:login')

def dashboard(request):
    return render(request, 'dashboard.html', {})