from rest_framework import generics, mixins
from .models import Snippet
from .serializers import SnippetSerializer


class SnippetList(mixins.ListModelMixin, mixins.CreateModelMixin,
                generics.GenericAPIView):
    """
    List all code snippets, or create new snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer

    def get(self, request, *args, *kwargs):
        return self.list(request,*args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class SnippetDetails(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """
    Retrieve, Update, Delete a code snippet
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
        
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
   
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)