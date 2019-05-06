from django.urls import path
from noticias.views import Noticias

urlpatterns = [
    path('noticias/', Noticias.as_view())
]