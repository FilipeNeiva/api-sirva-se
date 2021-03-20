from rest_framework import serializers
from fiado.models import Fiado, Devedor
from api_sirva_se.serializers import UserSerializer
from venda.serializers import ProdutoSerializer


class DevedorSerializer(serializers.HyperlinkedModelSerializer):
    mercearia = UserSerializer(many=False)
    
    class Meta:
        model = Devedor
        fields = ('id', 'mercearia', 'nome', 'telefone', 'cpf')

        
class FiadoSerializer(serializers.HyperlinkedModelSerializer):
    mercearia = UserSerializer(many=False)
    devedor = DevedorSerializer(many=False)
    produto = ProdutoSerializer(many=False)
    
    class Meta:
        model = Fiado
        fields = ('id', 'mercearia', 'devedor', 'produto', 'quantidade', 'data_hora')