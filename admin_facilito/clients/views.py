from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect

from forms import LoginForm
from forms import CreateUserForm
from forms import EditUserForm
from forms import EditPasswordForm

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as login_django, logout as logout_django
from django.contrib.auth.decorators import login_required

from django.views.generic import View, DetailView, CreateView
from django.views.generic.edit import UpdateView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth import update_session_auth_hash

# Create your views here.

class ShowView(DetailView):
    model           =  User
    template_name   = 'show.html'
    slug_field      = 'username'  #Campo de la base de datos por el que se va a traer la info
    slug_url_kwarg  = 'username_url' #Como se llama en la url.


class LoginView(View):
    form     = LoginForm()
    message  = None
    template = 'login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return redirect('client:dashboard')
        return render(request, self.template, self.get_context())

    def post(self, request, *args, **kwargs):
        username_post = request.POST['username']
        password_post = request.POST['password']

        # Se verifica si el usuario y contasena mandado existen dentro de la base de datos.
        user = authenticate(username=username_post, password=password_post)
        if user is not None:
            login_django(request, user)
            return redirect('client:dashboard')
        else:
            message = "Username o password incorrectos"
        return render(request, self.template, self.get_context())

    # Funcion para obtener el contexto
    def get_context(self):
        return {'form': self.form, 'message': self.message}
'''
def login_con_funcion(request):
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
'''

@login_required( login_url = 'client:login')
def logout(request):
    logout_django(request)
    return redirect('client:login')


class DashboardView(LoginRequiredMixin, View):
    login_url = 'client:login'

    def get(self, request, *args, **kwargs):
        return render(request, 'dashboard.html', {})
'''
# El login_required es para ingresar a la pagina unicamente si esta loggeado
@login_required( login_url = 'client:login') # Si no esta loggeado, lo manda a la de login.
def dashboard_function(request):
    # if request.user.is_authenticate()
    return render(request, 'dashboard.html', {})
'''


class Create(CreateView):
    success_url   = reverse_lazy('client:login') #reverse_lazy regresa toda la url de client:login
    model         = User
    template_name = 'create.html'
    form_class    = CreateUserForm

    # Se sobreescribe form_valid para la encriptacion del password
    def form_valid(self, form):
        self.object = form.save( commit = False )
        self.object.set_password( self.object.password )
        self.object.save()
        return HttpResponseRedirect( self.get_success_url() ) #REcupera la url de exito -- success_url   = 'client:login'


'''
def create(request):

    form = CreateUserForm(request.POST or None)  # El Request.POST permite poner la logica desde en la clase Forms y no en la View
    if request.method == 'POST':
        if form.is_valid():
            # Es en caso de que el password se muestre cuando se crea la cuenta.
            # Para guardar correctamente en la BD.
            user = form.save( commit = False )
            user.set_password( user.password )
            user.save()
            return redirect('client:login')

    context = {
        'form' : form
    }
    return render(request, 'create.html', context)
'''

class Edit(UpdateView):
    model = User
    template_name = 'edit.html'
    success_url   = reverse_lazy('client:dashboard')
    form_class    = EditUserForm

    def get_object(self, queryset = None):
        return self.request.user


def edit_password(request):
    message = None
    # En caso de que sea una solicitud POST, dentro de form se recuperan todos los datos del formulario.
    form = EditPasswordForm(request.POST or None)

    # Si es una solicitud POSt, se valida que la informacion es correcta
    if request.method == 'POST':
        if form.is_valid():
            current_password = form.cleaned_data['password'] # Obtiene los valores de la forma
            new_password = form.cleaned_data['new_password']

            # Despues de validar que la contrasena (formato) es valida, se verifica si la contrasena corresponde al usuario actual.
            if authenticate(username = request.user.username, password = current_password):
                request.user.set_password( new_password ) # Si si, se le actualiza la nueva contrasena
                request.user.save()
                # Se utiliza para continuar al usuario en su sesion
                update_session_auth_hash(request, request.user)
                message = "password actualizado"
            else:
                message = "Password invalido. No corresponde al usuario %s" %(request.user.username)


    context = {'form' : form, 'message': message}
    return render(request, 'edit_password.html', context)
