from django.urls import path
from club import views

urlpatterns = [
    path("", views.main, name="main"),
    path("saludo/<nombre>", views.saludo, name="saludo"),
]