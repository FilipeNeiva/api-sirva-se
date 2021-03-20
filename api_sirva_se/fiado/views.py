from django.shortcuts import render
from rest_framework import viewsets, permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from fiado.serializers import FiadoSerializer, DevedorSerializer
from fiado.models import Fiado, Devedor
from api_sirva_se.utils import pegar_usuario_por_token

# Create your views here.

class FiadoList(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = FiadoSerializer

    def get_queryset(self):
        app_tk = self.request.META["HTTP_AUTHORIZATION"]
        user = pegar_usuario_por_token(app_tk)

        return Fiado.objects.filter(mercearia=user)

    def perform_create(self, serializer):
        app_tk = self.request.META["HTTP_AUTHORIZATION"]
        user = pegar_usuario_por_token(app_tk)

        serializer.save(mercearia=user)

class DevedorList(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = DevedorSerializer

    def get_queryset(self):
        app_tk = self.request.META["HTTP_AUTHORIZATION"]
        user = pegar_usuario_por_token(app_tk)

        return Devedor.objects.filter(mercearia=user)

    def perform_create(self, serializer):
        app_tk = self.request.META["HTTP_AUTHORIZATION"]
        user = pegar_usuario_por_token(app_tk)

        serializer.save(mercearia=user)
    
    
