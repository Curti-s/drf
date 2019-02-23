from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework import generics, permissions
from rest_framework import renderers
from rest_framework.reverse import reverse
from rest_framework.response import Response
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

@api_view(['GET'])
def api_root(request, format=None):
    # using reverse to return fully qualified urls
    return Response({
        'users':reverse('user-list',request=request, format=format),
        'snippets':reverse('snippet-list', request=request, format=format)
    })

class SnippetHighlight(generics.GenericAPIView):
    """
    View for rendering a snippet object instance property
    """
    queryset = Snippet.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)
    
    def get(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet)