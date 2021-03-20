from django.contrib.auth.models import User, Group
from django.contrib import admin
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope

from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import (api_view, permission_classes, action)

from api_sirva_se.utils import pegar_usuario_por_token, pegar_contexto
from api_sirva_se.serializers import UserSerializer, GroupSerializer, UserRegistrationSerializer

admin.autodiscover()


# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    @action(detail=True, method=['post'], permission_classes=[permissions.AllowAny])
    def register(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        model_serializer = UserSerializer(data=serializer.data)
        model_serializer.is_valid(raise_exception=True)
        model_serializer.save()
        return Response(model_serializer.data)
    @action(detail=True, methods=['get'])
    def info(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
    def list(self, request):
        user = request.user
        if not user or not user.is_superuser:
            return HttpResponseForbidden()
        return super(UserViewSet, self).list(request)
    def update(self, request, pk=None):
        user = User.objects.filter(id=pk).first()
        if not user or request.user != user:
            return HttpResponseForbidden()
        return super(UserViewSet, self).update(request)


class UserRegister(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserRegistrationSerializer
    

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