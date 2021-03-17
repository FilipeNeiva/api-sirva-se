from django.contrib.auth.models import User, Group
from api_sirva_se.serializers import UserSerializer, GroupSerializer
from django.contrib import admin
from rest_framework.response import Response
admin.autodiscover()
from rest_framework import viewsets, permissions
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
from api_sirva_se.utils import pegar_usuario_por_token, pegar_contexto

# Create your views here.

class UserList(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

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