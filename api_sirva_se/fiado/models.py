from django.db import models
from django.contrib.auth.models import User
from venda.models import Produto, Mercearia

# Create your models here.


class Devedor(models.Model):
    mercearia = models.ForeignKey(Mercearia, null=True, blank=True, 
        on_delete=models.PROTECT, related_name='devedores_usuario')
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=14, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)


class Fiado(models.Model):
    mercearia = models.ForeignKey(Mercearia, null=True, blank=True, 
        on_delete=models.PROTECT, related_name='vendas_fiado')
    devedor = models.ForeignKey(Devedor, on_delete=models.PROTECT)
    data_hora = models.DateTimeField()
    

class ItemFiado(models.Model):
    fiado = models.ForeignKey(Fiado, on_delete=models.PROTECT,
        related_name='itens_fiado')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='produto_fiado')
    quantidade = models.IntegerField(default=1)
