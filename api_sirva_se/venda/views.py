from venda import models, serializers
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from oauth2_provider.contrib.rest_framework import TokenHasScope, TokenHasReadWriteScope
from api_sirva_se.utils import pegar_contexto, pegar_usuario_por_token


class VendaList(viewsets.ViewSet):
    class Meta:
        model = models.Venda

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
        else:
            permission_classes = [permissions.IsAdminUser]
        return[permission() for permission in permission_classes]
    
    def list(self, request):
        app_tk = request.META["HTTP_AUTHORIZATION"]
        user = pegar_usuario_por_token(app_tk)
        serializer_context = pegar_contexto()

        queryset = models.Venda.objects.filter(mercearia=user)

        serializer = serializers.VendaSerializer(queryset, context=serializer_context)
        return Response(serializer.data)


class VendaList2(generics.ListAPIView):
    serializer_class = serializers.VendaSerializer

    queryset = models.Venda.objects.all()

class VendaList3(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    serializer_class = serializers.VendaSerializer
    
    def get_queryset(self):
        app_tk = self.request.META["HTTP_AUTHORIZATION"]
        user = pegar_usuario_por_token(app_tk)
        
        return models.Venda.objects.filter(mercearia=user)
    

    


        