from django.db import models

class lista(models.Model):
    numero = models.IntegerField(unique=True)

class questao(models.Model):
    enunciado = models.CharField(max_length=255)
    alternativa1 = models.CharField(max_length=255)
    alternativa2 = models.CharField(max_length=255)
    alternativa3 = models.CharField(max_length=255)
    alternativacorreta = models.CharField(max_length=255)
    respondido = models.BooleanField()
    correto = models.BooleanField()
    listas = models.ManyToManyField(lista)