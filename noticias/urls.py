from django.urls import path
from noticias.views import VistaNoticias, VistaNota
from noticias.models import Nota

noticias_vista = VistaNoticias.as_view()
nota_vista = VistaNota.as_view()

urlpatterns = [
    path('noticias/<slug:slug>', nota_vista, name="nota"),
    path('noticias/', noticias_vista, name="noticias"),
]