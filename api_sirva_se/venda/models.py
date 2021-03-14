from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Produto(models.Model):
    nome = models.CharField(max_length=30)
    quantidade_em_estoque = models.IntegerField()
    valor_unidade = models.FloatField()


class Venda(models.Model):
    mercearia = models.ForeignKey(User, on_delete=models.PROTECT, related_name='vendas_mercearia')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='produto_venda')
    quantidade = models.IntegerField(default=1)
    data_hora = models.DateTimeField()