# Generated by Django 5.1.3 on 2024-11-13 17:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carteira',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('saldo', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Transacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('compra', 'Compra'), ('venda', 'Venda'), ('transferencia', 'Transferência'), ('movimentacao', 'Movimentação')], max_length=50)),
                ('valor', models.FloatField()),
                ('data', models.DateTimeField(auto_now_add=True)),
                ('origem', models.IntegerField()),
                ('destino', models.IntegerField()),
                ('carteira', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transacoes', to='wallet.carteira')),
            ],
        ),
    ]
