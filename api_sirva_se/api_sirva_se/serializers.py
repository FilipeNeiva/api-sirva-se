
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name',)
        write_only_fields = ('username',)
    def validate(self, data):
        # Making sure the username always matches the email
        email = data.get('email', None)
        if email:
            data['username'] = email
        return data


class UserRegistrationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    password = serializers.CharField()
    confirm_password = serializers.CharField()
    def validate_email(self, email):
        existing = User.objects.filter(email=email).first()
        if existing:
            raise serializers.ValidationError("Alguem com esse Endereço de email já registrado. Foi você?")
        return email
    def validate(self, data):
        if not data.get('password') or not data.get('confirm_password'):
            raise serializers.ValidationError("Por favor digite a senha e confirm it.")
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("As senhas não coincidem.")
        return data

    def create(self, validated_data):
        return User.objects.create(**validated_data)

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']