from django.contrib import admin
from django.urls import path, include

app_filmes = "filmes"

urlpatterns = [
    path("", include('filmes.urls')),
    path("admin/", admin.site.urls),
]
