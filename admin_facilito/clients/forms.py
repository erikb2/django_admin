from django import forms
from django.contrib.auth.models import User

'''
Constants
'''
ERROR_MESSAGE_USER = {'required': 'El username es requerido.', 'unique': 'El username ya se encuentra registrado.', 'invalid': 'El username es incorrecto.'}
ERROR_MESSAGE_PASSWORD = {'required': 'Password requerido'}
ERROR_MESSAGE_EMAIL = {'required': 'E-mail requerido', 'invalid':  'Correo electronico no es valido'}


'''
Functions
'''
def must_be_gt(value_password):
    if len(value_password) < 5:
        raise forms.ValidationError('El password debe contener una longitud de 5 como minimo')
    value_password

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

# El atributo validators se utiliza para encapsular las funciones que se deben de utilizar para validar los campos
class EditPasswordForm(forms.Form):
    # Obtiene los campos del formulario para cambiar la contrasena
    password        = forms.CharField(max_length=20, widget = forms.PasswordInput(), error_messages = ERROR_MESSAGE_PASSWORD)
    new_password    = forms.CharField(max_length=20, widget = forms.PasswordInput(), error_messages = ERROR_MESSAGE_PASSWORD, validators = [must_be_gt])
    repeat_password = forms.CharField(max_length=20, widget = forms.PasswordInput(), error_messages = ERROR_MESSAGE_PASSWORD, validators = [must_be_gt])

    # Metodo que se llama cuando se realiza el form.is_valid dentro de la vista
    def clean(self):
        clean_data = super(EditPasswordForm, self).clean()
        password1  = clean_data.get('new_password')
        password2  = clean_data.get('repeat_password')

        if password1 != password2:
            raise forms.ValidationError('El nuevo password no es el mismo que el de validacion')
