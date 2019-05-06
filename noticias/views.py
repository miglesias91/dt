from django.shortcuts import render
from django.views.generic import ListView

from noticias.models import Nota

class Noticias(ListView):
    model = Nota
