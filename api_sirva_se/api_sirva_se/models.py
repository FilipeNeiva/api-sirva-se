from django.db import models
from django.contrib.auth.models import User


class Produto(models.Model):
    nome = models.CharField(max_length=30)
    quantidade_em_estoque = models.IntegerField()
    valor_unidade = models.FloatField()