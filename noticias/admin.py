from django.contrib import admin
from .models import Nota, Periodista, Comentario

admin.site.register(Nota)
admin.site.register(Periodista)
admin.site.register(Comentario)