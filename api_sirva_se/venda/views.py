from venda import models, serializers
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from oauth2_provider.contrib.rest_framework import TokenHasScope, TokenHasReadWriteScope
from api_sirva_se.utils import pegar_contexto, pegar_usuario_por_token
from rest_framework.exceptions import APIException


class ProdutoListView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = serializers.ProdutoSerializer

    def get_queryset(self):
        app_tk = self.request.META["HTTP_AUTHORIZATION"]
        user = pegar_usuario_por_token(app_tk)

        return models.Produto.objects.filter(mercearia__usuario=user)

    def perform_create(self, serializer):
        app_tk = self.request.META["HTTP_AUTHORIZATION"]
        user = pegar_usuario_por_token(app_tk)

        serializer.save(mercearia=models.Mercearia.objects.get(usuario=user))

class VendaListView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = serializers.VendaSerializer
    
    def get_queryset(self):
        app_tk = self.request.META["HTTP_AUTHORIZATION"]
        user = pegar_usuario_por_token(app_tk)
        
        return models.Venda.objects.filter(mercearia__usuario=user)

    def perform_create(self, serializer):
        app_tk = self.request.META["HTTP_AUTHORIZATION"]
        user = pegar_usuario_por_token(app_tk)

        serializer.save(mercearia=models.Mercearia.objects.get(usuario=user))



class ItemVendaListView(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = serializers.ItemVendaSerializer

    def get_queryset(self):
        app_tk = self.request.META["HTTP_AUTHORIZATION"]
        user = pegar_usuario_por_token(app_tk)

        pk = self.kwargs['pk']
        venda = models.Venda.objects.get(id=pk)
        
        if venda.mercearia != models.Mercearia.objects.get(usuario=user):
            raise APIException('usuario não tem permição para acessar essa venda')
        
        return models.ItemVenda.objects.filter(venda=venda)
        