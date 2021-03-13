from django.contrib.auth.models import User, Group
from venda.serializers import UserSerializer, GroupSerializer
from django.contrib import admin
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

class GroupList(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, TokenHasScope]
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
