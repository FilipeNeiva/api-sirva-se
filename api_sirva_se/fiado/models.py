from django.db import models
from django.contrib.auth.models import User
from api_sirva_se.models import Produto

# Create your models here.


class Devedor(models.Model):
    mercearia = models.ForeignKey(User, on_delete=models.PROTECT, related_name='devedores_usuario')
    nome = models.CharField(max_length=30)
    telefone = models.CharField(max_length=14, null=True, blank=True)
    cpf = models.CharField(max_length=14, null=True, blank=True)


class Fiado(models.Model):
    mercearia = models.ForeignKey(User, on_delete=models.PROTECT, related_name='vendas_fiado')
    devedor = models.ForeignKey(Devedor, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='produto_fiado')
    quantidade = models.IntegerField(default=1)
    data_hora = models.DateTimeField()
