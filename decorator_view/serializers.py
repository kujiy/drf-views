from rest_framework import serializers

from decorator_view.models import Snippet1


class Snippet1Serializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet1
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']