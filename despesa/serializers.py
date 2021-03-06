from rest_framework import serializers
from despesa.models import *
from api_sirva_se.serializers import UserSerializer
from venda.serializers import ProdutoSerializer


class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = '__all__'


class ItemDespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemDespesa
        fields = '__all__'