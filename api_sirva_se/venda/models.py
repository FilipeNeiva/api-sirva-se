from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Produto(models.Model):
    mercearia = models.ForeignKey(User, blank=True, null=False, on_delete=models.PROTECT, 
        related_name='produtos_mercearia')
    nome = models.CharField(max_length=30)
    quantidade_em_estoque = models.IntegerField()
    valor_unidade = models.FloatField()
    valor_bruto = models.FloatField()


class Venda(models.Model):
    mercearia = models.ForeignKey(User, blank=True, null=False, on_delete=models.PROTECT, related_name='vendas_mercearia')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='produto_venda')
    quantidade = models.IntegerField(default=1)
    data_hora = models.DateTimeField(default=timezone.now)