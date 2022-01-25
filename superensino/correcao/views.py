from django.shortcuts import render
from rest_framework import viewsets
from .serializers import questaoSerializer
from .models import questao, lista
from rest_framework import generics
from django.http.response import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
import json

class listaViewSet(viewsets.ModelViewSet):
    queryset = lista.objects.all().order_by('id')
    serializer_class = questaoSerializer

class questaoViewSet(viewsets.ModelViewSet):
    queryset = questao.objects.all().order_by('id')
    serializer_class = questaoSerializer

class respondidasViewSet(viewsets.ModelViewSet):
    serializer_class = questaoSerializer   
    queryset = questao.objects.filter(respondido = True)

class corretasViewSet(viewsets.ModelViewSet):
    serializer_class = questaoSerializer  
    queryset = questao.objects.filter(correto = True)

