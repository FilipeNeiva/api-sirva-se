from django.db import models
from django.contrib.auth.models import User
from api_sirva_se.models import Produto

# Create your models here.


class Despesa(models.Model):
    mercearia = models.ForeignKey(User, on_delete=models.PROTECT, related_name='despesas_usuario')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT, related_name='produto_despesa')
    quantidade = models.IntegerField(default=1)