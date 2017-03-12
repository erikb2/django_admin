from django import forms
from django.contrib.auth.models import User

# Clase para generar el form de un login
class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget = forms.PasswordInput())


class CreateUserForm(forms.ModelForm):

    username = forms.CharField(
        max_length=20, 
        error_messages = {'required': 'El username es requerido.',
                          'unique': 'El username ya se encuentra registrado.',
                          'invalid': 'El username es incorrecto.'}
        )
    password = forms.CharField(
        max_length=20, widget = forms.PasswordInput(),
        error_messages = {'required': 'Password requerido'}
        )
    email    = forms.CharField(
        error_messages = {'required': 'E-mail requerido',
                          'invalid':  'Correo electronico no es valido',
                         }
        )
    class Meta:
        model = User 
        fields = ('username', 'password', 'email')