from django import forms
from django.contrib.auth.models import User

'''
Constants
'''
ERROR_MESSAGE_USER = {'required': 'El username es requerido.', 'unique': 'El username ya se encuentra registrado.', 'invalid': 'El username es incorrecto.'}
ERROR_MESSAGE_PASSWORD = {'required': 'Password requerido'}
ERROR_MESSAGE_EMAIL = {'required': 'E-mail requerido', 'invalid':  'Correo electronico no es valido'}


'''
Class
'''
# Clase para generar el form de un login
class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget = forms.PasswordInput())


class CreateUserForm(forms.ModelForm):

    username = forms.CharField(
        max_length=20,
        error_messages = ERROR_MESSAGE_USER
        )
    password = forms.CharField(
        max_length=20, widget = forms.PasswordInput(),
        error_messages = ERROR_MESSAGE_PASSWORD
        )
    email    = forms.CharField(
        error_messages = ERROR_MESSAGE_EMAIL
        )
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class EditUserForm(forms.ModelForm):

    username = forms.CharField(
        max_length=20,
        error_messages = ERROR_MESSAGE_USER
        )
    email    = forms.CharField(
        error_messages = ERROR_MESSAGE_EMAIL
        )

    class Meta:
        model  = User
        fields = ('username', 'email', 'first_name', 'last_name')
