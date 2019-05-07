from django.shortcuts import render
from django.views.generic import ListView, DetailView

from noticias.models import Nota

class VistaNoticias(ListView):
    queryset = Nota.objects.order_by("-fecha")
    paginate_by = 5
    template_name = "noticias/noticias.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class VistaNota(DetailView):
    model = Nota
    context_object_name = "nota"
    template_name = "noticias/nota.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context