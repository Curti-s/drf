from rest_framework import generics
from .models import Snippet
from .serializers import SnippetSerializer


class SnippetList(generics.ListCreateAPIView):
    """
    List all code snippets, or create new snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

class SnippetDetails(generics.RetrieveDestroyAPIView):
    """
    Retrieve, Update, Delete a code snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    