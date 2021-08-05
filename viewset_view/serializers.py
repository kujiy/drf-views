from rest_framework import serializers

from viewset_view.models import Snippet4


class Snippet4Serializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet4
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']