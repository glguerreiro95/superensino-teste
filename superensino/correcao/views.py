from rest_framework import viewsets
from .serializers import questaoSerializer
from .models import questao, lista
from django.http.response import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
import json

class questaoViewSet(viewsets.ModelViewSet):
    queryset = questao.objects.all().order_by('id')
    serializer_class = questaoSerializer

def resumo_exercicios(self, *args, **kwargs):
    banco = questao.objects.all().count()
    certas = questao.objects.filter(respondido = True, correto = True).count()
    total = questao.objects.filter(respondido = True).count()
    valor = (certas/total)*100
    erradas = total - certas
    response = {'total de questões no banco': banco,'total de questões respondidas': total, 'total de respostas corretas': certas,
    'proporção entre respostas corretas e respondidas': str(valor) + '%', 'total de respostas erradas': erradas}
    return HttpResponse(json.dumps(response, sort_keys=True, indent=1, cls=DjangoJSONEncoder), content_type='application/json')

def exercicios_por_lista(self, *args, **kwargs):
    id_lista = self.GET['id_lista']
    lista_aux = questao.objects.filter(listas = id_lista).values()
    questoes = list(lista_aux)
    total = lista_aux.count()
    certas = lista_aux.filter(correto = True, respondido = True).count()
    respondidas = lista_aux.filter(respondido = True).count()
    proporcao = (certas/total)*100
    erradas = total-certas
    response = {'total de questões na lista': total, 'total de questões respondidas': respondidas, 'total de respostas certas': certas, 
    'proporção de respostas certas': str(proporcao) + '%', 'total de questões erradas': erradas, 'questões': questoes}
    return HttpResponse(json.dumps(response, sort_keys=True, indent=1, cls=DjangoJSONEncoder), content_type='application/json')



