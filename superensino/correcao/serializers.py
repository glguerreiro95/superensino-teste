from rest_framework import serializers
from .models import questao, lista

class questaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = questao
        fields = ('enunciado', 'alternativa1', 'alternativa2', 'alternativa3', 'alternativacorreta')

class listaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = lista
        fields = ('questoes')