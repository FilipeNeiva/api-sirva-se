from django.contrib.auth.models import User, Group
from django.contrib import admin
from django.http import HttpResponseForbidden
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.decorators import (api_view, permission_classes, action)

from venda.models import Mercearia
from api_sirva_se.utils import pegar_usuario_por_token, pegar_contexto
from api_sirva_se.serializers import *

admin.autodiscover()


# Create your views here.

class UserRegister(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserRegistrationSerializer
    

class MerceariaRegister(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Mercearia.objects.all()
    serializer_class = MerceariaCreateSerializer


class GetMercearia(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = MerceariaListSerializer
    model = serializer_class.Meta.model
    def get_queryset(self):
        app_tk = self.request.META["HTTP_AUTHORIZATION"]
        user  = pegar_usuario_por_token(app_tk)

        return Mercearia.objects.filter(usuario=user)

class GetUser(viewsets.ViewSet):
    class Meta:
        model = User
    
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
        else:
            permission_classes = [permissions.IsAdminUser]
        return[permission() for permission in permission_classes]
    
    def list(self, request):
        #Pegando o token utilizado
        app_tk = request.META["HTTP_AUTHORIZATION"]
        user = pegar_usuario_por_token(app_tk)
        serializer_context = pegar_contexto()
        
        serializer = UserSerializer(instance=user, context=serializer_context)
        return Response(serializer.data)
