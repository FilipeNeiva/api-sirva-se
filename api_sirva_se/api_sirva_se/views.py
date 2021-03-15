from django.contrib.auth.models import User, Group
from api_sirva_se.serializers import UserSerializer, GroupSerializer
from django.contrib import admin
from oauth2_provider.models import AccessToken
import re
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
admin.autodiscover()

from rest_framework import viewsets, permissions

from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

# Create your views here.

class UserList(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class UserDetails(viewsets.ModelViewSet):
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

        #Pegando o usuario pelo token
        m = re.search('(Bearer)(\s)(.*)', app_tk)
        app_tk = m.group(3)
        acc_tk = AccessToken.objects.get(token=app_tk)
        user = acc_tk.user

        queryset = User.objects.get(id=user.id)

        #Pegando o contexto do serializer
        factory = APIRequestFactory()
        requeste = factory.get('/')
        serializer_context = {
            'request': Request(requeste),
        }

        serializer = UserSerializer(instance=user, context=serializer_context)
        return Response(serializer.data)