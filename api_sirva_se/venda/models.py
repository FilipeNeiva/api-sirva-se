from django.db import models
from django.contrib.auth.models import User
from api_sirva_se.models import Produto

# Create your models here.


class Venda(models.Model):
    mercearia = models.ForeignKey(User, on_delete=models.PROTECT, related_name='vendas_mercearia')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='produto_venda')
    quantidade = models.IntegerField(default=1)
    data_hora = models.DateTimeField()