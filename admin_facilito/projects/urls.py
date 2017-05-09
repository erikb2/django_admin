from django.conf.urls import url
from . import views

app_name = 'project'
urlpatterns = [
    url(r'^create/$', views.CreateClass.as_view(), name="create"),
    url(r'^my_projects/$', views.ListClass.as_view(), name="my_projects"),
    url(r'^show/(?P<slug>[\w-]+)/$', views.ShowClass.as_view(), name="show"),
    url(r'^edit/(?P<slug>[\w-]+)/$', views.edit, name="edit"),
]
