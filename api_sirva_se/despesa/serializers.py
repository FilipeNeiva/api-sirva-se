from rest_framework import serializers
from despesa.models import Despesa
from api_sirva_se.serializers import UserSerializer
from venda.serializers import ProdutoSerializer


class DespesaSerializer(serializers.HyperlinkedModelSerializer):
    mercearia = UserSerializer(many=False)
    produto = ProdutoSerializer(many=False)
    class Meta:
        model = Despesa
        fields = ('id', 'mercearia', 'produto', 'quantidade')