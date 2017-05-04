from django.shortcuts import render

from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin # Valida si el usuario esta loggeado

# Create your views here.
class CreateClass(CreateView, LoginRequiredMixin):
    pass
