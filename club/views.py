import re
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def main(request):
    return render(
        request,
        'club/club.html'
    )

def saludo(request, nombre):
    return render(
        request,
        'club/saludo.html',
        {
            'nombre': nombre,
            'fecha' : datetime.now()
        }
    )

def torneos(request):
    return render(
        request,
        'club/torneos.html'
    )

def equipo(request):
    return render(
        request,
        'club/equipo.html'
    )