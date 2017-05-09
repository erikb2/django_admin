from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin  # Valida si el usuario esta loggeado
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required

from status.models import Status
from .models import Project

from .forms import ProjectForm

# Create your views here.


class CreateClass(LoginRequiredMixin, CreateView):
    login_url     = 'client:login'
    template_name = 'project/create.html'
    model         = Project
    form_class    = ProjectForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        self.object.projectstatus_set.create(status=Status.get_default_status())
        return HttpResponseRedirect(self.get_url_project())

    def get_url_project(self):
        return reverse_lazy('project:show', kwargs={'slug': self.object.slug})


# Clase utilizada para Listar los proyectos creados por el usuario actual


class ListClass(LoginRequiredMixin, ListView):
    login_url     = 'client:login'
    template_name = 'project/own.html'

    # Query que define los registros que se trae a traves del filter de la tabla Project
    def get_queryset(self):
        return Project.objects.filter(user=self.request.user).order_by('dead_line')


class ShowClass(LoginRequiredMixin, DetailView):
    login_url       = 'client:login'
    model           = Project
    template_name   = 'project/show.html'


"""
Functions
"""


@login_required(login_url='client:login')
def edit(request, slug=''):
    project = get_object_or_404(Project, slug=slug)
    form_project = ProjectForm(request.POST or None, instance=project)
    context = {
        'form_project': form_project
    }
    return render(request, 'project/edit.html', context)
    
