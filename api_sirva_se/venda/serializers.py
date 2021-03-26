from venda.models import *
from rest_framework import serializers
from api_sirva_se.serializers import UserSerializer


class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = '__all__'


class VendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Venda
        fields = '__all__'

class ItemVendaSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemVenda
        fields = '__all__'