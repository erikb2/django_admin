from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def show(request):
    return HttpResponse("Prueba correcta")


def login(request):
    nombre = 'Erik'
    edad   = 12
    context = {'nombre' : nombre, 'edad': edad }
    return render(request, 'login.html', context)