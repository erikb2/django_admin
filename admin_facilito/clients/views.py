from django.shortcuts import render, redirect
from django.http import HttpResponse
from forms import LoginForm
from forms import CreateUserForm
from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from django.contrib.auth.decorators import login_required

# Create your views here.
def show(request):
    return HttpResponse("Prueba correcta")


def login(request):
    # Primero verifica que en caso de que el usuario este
    # logueado, lo regresa a la ventana de dashboard
    if request.user.is_authenticated():
        return redirect('client:dashboard')

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

@login_required( login_url = 'client:login')
def logout(request):
    logout_django(request)
    return redirect('client:login')

# El login_required es para ingresar a la pagina unicamente si esta loggeado
@login_required( login_url = 'client:login') # Si no esta loggeado, lo manda a la de login.
def dashboard(request):
    # if request.user.is_authenticate()
    return render(request, 'dashboard.html', {})


def create(request):
    form = CreateUserForm()
    context = {
        'form' : form
    }
    return render(request, 'create.html', context)