from rest_framework import serializers
from fiado.models import *
from api_sirva_se.serializers import UserSerializer
from venda.serializers import ProdutoSerializer


class DevedorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Devedor
        fields = '__all__'

        
class FiadoSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Fiado
        fields = '__all__'


class ItemFiadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemFiado
        fields = '__all__'