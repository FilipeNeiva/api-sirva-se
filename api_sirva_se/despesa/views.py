from django.shortcuts import render
from rest_framework import viewsets, permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from despesa.serializers import DespesaSerializer
from despesa.models import Despesa
from api_sirva_se.utils import pegar_usuario_por_token

# Create your views here.

class DespesaList(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = DespesaSerializer

    def get_queryset(self):
        app_tk = self.request.META["HTTP_AUTHORIZATION"]
        user  = pegar_usuario_por_token(app_tk)

        return Despesa.objects.filter(mercearia=user)
    