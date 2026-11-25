from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="inicio"),
    path("login/", views.login_view, name="login"),
    path("panel/", views.panel, name="panel"),
]