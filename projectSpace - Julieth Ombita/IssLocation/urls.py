from django.urls import path
from . import views


urlpatterns = [
    path("", views.say_hello, name="home"),
    path("ISSlocation/", views.ISSlocation, name="ISSlocation"),
    path("humanInSpace/", views.humanInSpace, name="humanInSpace"),
]
