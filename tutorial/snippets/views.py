from django.contrib.auth.models import User
from rest_framework import generics, permissions
from .models import Snippet
from .serializers import SnippetSerializer, UserSerializer
from .permissions import IsOwnerReadOnly

class SnippetList(generics.ListCreateAPIView):
    """
    List all code snippets, or create new snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self,serializer):
        serializer.save(owner=self.request.user)

class SnippetDetails(generics.RetrieveDestroyAPIView):
    """
    Retrieve, Update, Delete a code snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_class = (permissions.IsAuthenticatedOrReadOnly,IsOwnerReadOnly,)

class UserList(generics.ListAPIView):
    """
    List all users
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    """
    Retrieve a single user
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer