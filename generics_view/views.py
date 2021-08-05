from generics_view.models import Snippet3
from generics_view.serializers import Snippet3Serializer
from rest_framework import generics


class SnippetList(generics.ListCreateAPIView):
    queryset = Snippet3.objects.all()
    serializer_class = Snippet3Serializer


class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet3.objects.all()
    serializer_class = Snippet3Serializer
