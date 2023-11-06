from django.contrib.auth.models import User
from rest_framework import viewsets
from eventproject.users.serializers import UserSerializer
from rest_framework import filters

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    filter_backends = [filters.SearchFilter]

    search_fields = ["id", 'username', 'email', 'password']


