import re
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def main(request):
    return HttpResponse("Deportivo Tachito")

def saludo(request, nombre):
    hora_y_fecha = datetime.now()
    hora_y_fecha_con_formato = hora_y_fecha.strftime("%A, %d %B, %Y at %X")

    # Filter the name argument to letters only using regular expressions. URL arguments
    # can contain arbitrary text, so we restrict to safe characters only.
    match_object = re.match("[a-zA-Z]+", nombre)

    if match_object:
        nombre_limpio = match_object.group(0)
    else:
        nombre_limpio = "amigo"

    content = "Bienvenido, " + nombre_limpio + "! Son las " + hora_y_fecha_con_formato
    return HttpResponse(content)