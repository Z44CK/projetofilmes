from django.urls import path
from .import views

app_filmes = "filmes"

urlpatterns = [
    path("", views.homepage, name="homepage"),
]
