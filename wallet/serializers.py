from rest_framework import serializers
from .models import Carteira, Transacao

class CarteiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carteira
        fields = ['id', 'nome', 'saldo']

class TransacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transacao
        fields = ['id','origem', 'destino', 'carteira', 'tipo', 'valor', 'data']
