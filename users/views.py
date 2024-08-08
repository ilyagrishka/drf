from django.shortcuts import render

from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from tutorial.quickstart.serializers import UserSerializer

from users.models import User


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()
