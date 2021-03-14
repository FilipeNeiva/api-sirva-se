from rest_framework import serializers
from fiado.models import Fiado, Devedor

class FiadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Fiado
        fields = '__all__'


class DevedorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Devedor
        fields = '__all__'