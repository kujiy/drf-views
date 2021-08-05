from rest_framework import serializers

from views_apiview.models import Snippet2


class Snippet2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet2
        fields = ['id', 'title', 'code', 'linenos', 'language', 'style']