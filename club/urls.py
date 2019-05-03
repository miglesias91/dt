from django.urls import path
from club import views

urlpatterns = [
    path("", views.main, name="main"),
    path("saludo/<nombre>", views.saludo, name="saludo"),
    path("equipo/", views.equipo, name="equipo"),
    path("torneos/", views.torneos, name="torneos"),
]