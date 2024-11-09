'''
views for user api
'''

from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from user.serializers import (
    UserSerializer,
    AuthTokenSerializer,
)


class CreateUserView(generics.CreateAPIView):
    '''create new user in system'''
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    '''create a new auth token for user'''
    serialzer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
