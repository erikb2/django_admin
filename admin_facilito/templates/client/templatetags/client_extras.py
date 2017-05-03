from django import template


def title_say_hello(username):
    return "Hola usuario: " + username.title()

register = template.Library()
register.filter('saluda', title_say_hello)
