from django.shortcuts import render
from rest_framework import viewsets, permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from despesa.serializers import *
from despesa.models import Despesa
from venda.models import Mercearia
from api_sirva_se.utils import pegar_usuario_por_token

# Create your views here.

class DespesaList(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = DespesaSerializer

    def get_queryset(self):
        app_tk = self.request.META["HTTP_AUTHORIZATION"]
        user  = pegar_usuario_por_token(app_tk)

        return Despesa.objects.filter(mercearia__usuario=user)

    def perform_create(self, serializer):
        app_tk = self.request.META["HTTP_AUTHORIZATION"]
        user = pegar_usuario_por_token(app_tk)

        serializer.save(mercearia=models.Mercearia.objects.get(usuario=user))


class ItemDespesaListView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = ItemDespesaSerializer

    def get_queryset(self):
        app_tk = self.request.META["HTTP_AUTHORIZATION"]
        user = pegar_usuario_por_token(app_tk)

        pk = self.kwargs['pk']
        despesa = Despesa.objects.get(id=pk)

        if despesa.mercearia != models.Mercearia.objects.get(usuario=user):
            raise APIException('usuario não tem permição para acessar essa despesa')

        return ItemDespesa.objects.filter(despesa=despesa)
    