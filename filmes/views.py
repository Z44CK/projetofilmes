from django.shortcuts import render
from .models import projetofilmes


def homepage(request):
    return render(
        request=request,
        template_name="lista_filmes.html",
        context={"Filmes": projetofilmes.objects.all}
    )
