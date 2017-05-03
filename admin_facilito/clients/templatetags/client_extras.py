from django import template


def title_say_hello(username):
    return "Hola usuario %s" %username

register = template.Library()
register.filter('saluda', title_say_hello)
