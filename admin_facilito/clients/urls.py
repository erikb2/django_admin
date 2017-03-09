from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^show/$', views.show, name="show"),
    url(r'^login/$', views.login, name="login"),
]