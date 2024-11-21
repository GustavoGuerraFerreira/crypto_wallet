from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Carteira, Transacao
from .serializers import CarteiraSerializer, TransacaoSerializer

class CarteiraViewSet(viewsets.ModelViewSet):
    queryset = Carteira.objects.all()
    serializer_class = CarteiraSerializer

    @action(detail=True, methods=['get'])
    def saldo(self, request, pk=None):
        carteira = self.get_object()
        return Response({"id": carteira.id, "saldo": carteira.saldo})

    @action(detail=True, methods=['put'])
    def movimentacao(self, request, pk=None):
        carteira = self.get_object()
        valor = request.data.get('valor', 0)
        carteira.saldo += float(valor)
        carteira.save()

        # Registra a transação
        transacao = Transacao.objects.create(
            carteira=carteira,
            tipo='movimentacao',
            valor=valor
        )

        return Response({"id": carteira.id, "saldo": carteira.saldo})



class TransacaoViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Transacao.objects.all()
    serializer_class = TransacaoSerializer

    def get_queryset(self):
        carteira_id = self.kwargs.get('carteira_pk')
        return self.queryset.filter()
    
    @action(detail=False, methods=['post'])
    def transferencia(self, request):
        print( request.data)
        origem_id = request.data.get('origem')
        destino_id = request.data.get('destino')
        valor = float(request.data.get('valor', 0))
        print( request.data.get('destino'))

        carteira_origem = Carteira.objects.get(id=origem_id)
        carteira_destino = Carteira.objects.get(id=destino_id)

        if carteira_origem.saldo >= valor:
            carteira_origem.saldo -= valor
            carteira_destino.saldo += valor
            carteira_origem.save()
            carteira_destino.save()

            # Registra a transação
            Transacao.objects.create(carteira=carteira_origem, tipo='transferencia_saida', valor=-valor, origem =origem_id, destino = destino_id )
            Transacao.objects.create(carteira=carteira_destino, tipo='transferencia_entrada', valor=valor, origem =origem_id, destino = destino_id )

            return Response({"status": "sucesso"}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "falha", "mensagem": "Saldo insuficiente"}, status=status.HTTP_400_BAD_REQUEST)
