from venda import models, serializers
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from oauth2_provider.contrib.rest_framework import TokenHasScope, TokenHasReadWriteScope
from api_sirva_se.utils import pegar_contexto, pegar_usuario_por_token


class VendaList(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = serializers.VendaSerializer
    
    def get_queryset(self):
        app_tk = self.request.META["HTTP_AUTHORIZATION"]
        user = pegar_usuario_por_token(app_tk)
        
        return models.Venda.objects.filter(mercearia=user)
    

    


        