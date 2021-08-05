from rest_framework import viewsets

from viewset_view.models import Snippet4
from viewset_view.serializers import Snippet4Serializer


class Snippet4ViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Snippet4.objects.all()
    serializer_class = Snippet4Serializer