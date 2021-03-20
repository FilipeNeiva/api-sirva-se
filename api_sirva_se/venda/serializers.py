from venda.models import Venda, Produto
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