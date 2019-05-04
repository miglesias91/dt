from django.urls import path
from club import views
from club.models import LogMessage

home_list_view = views.HomeListView.as_view(
    queryset=LogMessage.objects.order_by("-log_date")[:5],  # :5 limits the results to the five most recent
    context_object_name="message_list",
    template_name="club/club.html",
)

urlpatterns = [
    path("", home_list_view, name="main"),
    path("saludo/<nombre>", views.saludo, name="saludo"),
    path("equipo/", views.equipo, name="equipo"),
    path("torneos/", views.torneos, name="torneos"),
    path("log/", views.log_message, name="log"),
]