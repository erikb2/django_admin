from django import forms

# Clase para generar el form de un login
class LoginForm(forms.Form):
    username = forms.CharField(max_length=20)
    password = forms.CharField(max_length=20, widget = forms.PasswordInput)
