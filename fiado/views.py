from django.shortcuts import render
from rest_framework import viewsets, permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from fiado.serializers import *
from fiado.models import Fiado, Devedor
from venda.models import Mercearia
from api_sirva_se.utils import pegar_usuario_por_token

# Create your views here.

class FiadoList(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = FiadoSerializer

    def get_queryset(self):
        app_tk = self.request.META["HTTP_AUTHORIZATION"]
        user = pegar_usuario_por_token(app_tk)

        return Fiado.objects.filter(mercearia__usuario=user)

    def perform_create(self, serializer):
        app_tk = self.request.META["HTTP_AUTHORIZATION"]
        user = pegar_usuario_por_token(app_tk)

        serializer.save(mercearia=models.Mercearia.objects.get(usuario=user))

class DevedorList(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = DevedorSerializer

    def get_queryset(self):
        app_tk = self.request.META["HTTP_AUTHORIZATION"]
        user = pegar_usuario_por_token(app_tk)

        return Devedor.objects.filter(mercearia__usuario=user)

    def perform_create(self, serializer):
        app_tk = self.request.META["HTTP_AUTHORIZATION"]
        user = pegar_usuario_por_token(app_tk)

        serializer.save(mercearia=models.Mercearia.objects.get(usuario=user))


class ItemFiadoListView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = ItemFiadoSerializer

    def get_queryset(self):
        app_tk = self.request.META["HTTP_AUTHORIZATION"]
        user = pegar_usuario_por_token(app_tk)

        pk = self.kwargs['pk']
        fiado = Fiado.objects.get(id=pk)

        if fiado.mercearia != models.Mercearia.objects.get(usuario=user):
            raise APIException('usuario não tem permição para acessar essa venda fiado')

        return ItemFiado.objects.filter(fiado=fiado)
    
    
