from rest_framework import serializers
from back.models import Images

class ImagesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Images
        fields = ('image', 'created','mac')