from django.conf.urls import url
from . import views

app_name = 'project'
urlpatterns = [
    url(r'^create/$', views.CreateClass.as_view(), name="create"),
]