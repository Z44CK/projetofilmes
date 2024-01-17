from django.db import models


class projetofilmes(models.Model):
    titulo = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    descricao = models.TextField()

    def __str__(self):
        return self.titulo
