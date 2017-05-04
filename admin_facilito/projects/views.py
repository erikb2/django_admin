from django.shortcuts import render

from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin # Valida si el usuario esta loggeado

from .models import Project

from .forms import ProjectForm

# Create your views here.
class CreateClass(CreateView, LoginRequiredMixin):
    login_url     = 'client:login'
    template_name = 'project/create.html'
    model         = Project
    form_class    = ProjectForm
