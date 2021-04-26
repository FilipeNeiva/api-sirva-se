from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Mercearia(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    foto_perfil = models.ImageField(upload_to='perfil', default='imagem_perfil_default.png')


class Marca(models.Model):
    mercearia = models.ForeignKey(Mercearia, blank=True, null=False, on_delete=models.PROTECT, 
        related_name='marca_mercearia')
    nome = models.CharField(max_length=20)

class Produto(models.Model):
    mercearia = models.ForeignKey(Mercearia, blank=True, null=False, on_delete=models.PROTECT, 
        related_name='produtos_mercearia')
    nome = models.CharField(max_length=30)
    foto_produto = models.ImageField(upload_to='produtos', default='produto_default.jpg')
    quantidade_em_estoque = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name='marca_produto', null=True, blank=True)
    valor_unidade = models.FloatField()
    valor_bruto = models.FloatField()


class Venda(models.Model):
    mercearia = models.ForeignKey(Mercearia, blank=True, null=False, on_delete=models.PROTECT, related_name='vendas_mercearia')
    data_hora = models.DateTimeField(default=timezone.now)


class ItemVenda(models.Model):
    venda = models.ForeignKey(Venda, on_delete=models.PROTECT, related_name='itens')
    produto = models.ForeignKey(Produto, blank=True, null=True, on_delete=models.PROTECT,
        related_name='produto_item')
    quantidade = models.IntegerField()