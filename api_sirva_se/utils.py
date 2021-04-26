from oauth2_provider.models import AccessToken
import re
from django.contrib.auth.models import User
from rest_framework.test import APIRequestFactory
from rest_framework.request import Request


def pegar_usuario_por_token(token):
    m = re.search('(Bearer)(\s)(.*)', token)
    app_tk = m.group(3)
    acc_tk = AccessToken.objects.get(token=app_tk)
    user = acc_tk.user

    return user

def pegar_contexto():
    factory = APIRequestFactory()
    requeste = factory.get('/')
    serializer_context = {
        'request': Request(requeste),
    }

    return serializer_context