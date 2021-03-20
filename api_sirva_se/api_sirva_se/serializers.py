
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name',)


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