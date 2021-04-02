
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from venda.models import Mercearia

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name',)


class MerceariaListSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UserSerializer(many=False)
    class Meta:
        model = Mercearia
        fields = ('usuario', 'foto_perfil')


class MerceariaCreateSerializer(serializers.HyperlinkedModelSerializer):
    usuario = UserSerializer(many=False)
    class Meta:
        model = Mercearia
        fields = ('usuario', 'foto_perfil')

    def create(self, validate_data):
        usuario_data = validate_data.pop('usuario', None)
        existing = User.objects.filter(email=usuario_data['email']).first()
        if existing:
            raise serializers.ValidationError("Alguem com esse Endereço de email já registrado. Foi você?")
        if usuario_data:
            usuario = User.objects.create(username=usuario_data['email'],**usuario_data)
            validate_data['usuario'] = usuario

        return Mercearia.objects.create(**validate_data)


class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    password = serializers.CharField()
    def validate_email(self, email):
        existing = User.objects.filter(email=email).first()
        if existing:
            raise serializers.ValidationError("Alguem com esse Endereço de email já registrado. Foi você?")
        return email

    def create(self, validated_data):
        return User.objects.create(username=validated_data['email'], **validated_data)

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']