from rest_framework import viewsets, mixins
from .serializers import RegisterSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny


class RegisterViewSet(mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
        This class used to register a user
    """
    serializer_class = RegisterSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny,]