from django.db import models

class Carteira(models.Model):
    nome = models.CharField(max_length=50)
    saldo = models.FloatField(default=0.0)

    def __str__(self):
        return self.nome

class Transacao(models.Model):
    TIPO_CHOICES = (
        ('compra', 'Compra'),
        ('venda', 'Venda'),
        ('transferencia', 'Transferência'),
        ('movimentacao', 'Movimentação'),
    )
    carteira = models.ForeignKey(Carteira, on_delete=models.CASCADE, related_name="transacoes")
    tipo = models.CharField(max_length=50, choices=TIPO_CHOICES)
    valor = models.FloatField()
    data = models.DateTimeField(auto_now_add=True)
    origem= models.IntegerField()
    destino= models.IntegerField()
