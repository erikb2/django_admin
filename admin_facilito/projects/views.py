from django.shortcuts import render

from django.views.generic import CreateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin # Valida si el usuario esta loggeado
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy

from .models import Project

from .forms import ProjectForm

# Create your views here.
class CreateClass(LoginRequiredMixin, CreateView):
    login_url     = 'client:login'
    success_url   = reverse_lazy('client:dashboard')
    template_name = 'project/create.html'
    model         = Project
    form_class    = ProjectForm

    def form_valid(self, form):
        self.object = form.save(commit = False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect( self.get_success_url() )

class ListClass( LoginRequiredMixin, ListView):
    login_url     = 'client:login'
    template_name = 'project/own.html'

    def get_queryset(self):
        return Project.objects.filter(user = self.request.user).order_by('dead_line')
