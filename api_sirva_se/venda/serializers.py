from venda.models import Venda, Produto
from rest_framework import serializers


class VendaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'

class ProdutoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'