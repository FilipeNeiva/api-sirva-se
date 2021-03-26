from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Mercearia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.PROTECT, 
        related_name='mercearia_usuario')
    foto_perfil = models.ImageField()


class Produto(models.Model):
    mercearia = models.ForeignKey(User, blank=True, null=False, on_delete=models.PROTECT, 
        related_name='produtos_mercearia')
    nome = models.CharField(max_length=30)
    quantidade_em_estoque = models.IntegerField()
    valor_unidade = models.FloatField()
    valor_bruto = models.FloatField()


class Venda(models.Model):
    mercearia = models.ForeignKey(User, blank=True, null=False, on_delete=models.PROTECT, related_name='vendas_mercearia')
    data_hora = models.DateTimeField(default=timezone.now)


class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.PROTECT, related_name='itens')
    produto = models.ForeignKey(Produto, blank=True, null=True, on_delete=models.PROTECT,
        related_name='produto_item')
    quantidade = models.IntegerField()