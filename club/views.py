import re
from datetime import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView

from club.forms import LogMessageForm
from club.models import LogMessage

class HomeListView(ListView):
    """Renders the home page, with a list of all messages."""
    model = LogMessage

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

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

def log_message(request):
    form = LogMessageForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            message = form.save(commit=False)
            message.log_date = datetime.now()
            message.save()
            return redirect("main")
    else:
        return render(request, "club/mensaje_log.html", {"form": form})