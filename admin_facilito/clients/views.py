from django.shortcuts import render
from django.http import HttpResponse
from forms import LoginForm

# Create your views here.
def show(request):
    return HttpResponse("Prueba correcta")


def login(request):
    # Si nos estan enviando el formulario .:.
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        print username
        print password

    form = LoginForm()
    context = {
        'form': form
    }
    return render(request, 'login.html', context)