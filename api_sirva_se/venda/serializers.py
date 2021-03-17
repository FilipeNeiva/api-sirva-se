from venda.models import Venda, Produto
from rest_framework import serializers
from api_sirva_se.serializers import UserSerializer


class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
    mercearia = UserSerializer(many=False)

    class Meta:
        model = Produto
        fields = ('id', 'mercearia', 'nome', 'quantidade_em_estoque', 'valor_unidade', 'valor_bruto')


class VendaSerializer(serializers.HyperlinkedModelSerializer):
    mercearia = UserSerializer(many=False)
    produto = ProdutoSerializer(many=False)

    class Meta:
        model = Venda
        fields = ('id', 'mercearia', 'produto', 'quantidade', 'data_hora')