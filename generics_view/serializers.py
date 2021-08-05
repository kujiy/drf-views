from rest_framework import serializers

from generics_view.models import Snippet3


class Snippet3Serializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet3
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']