from rest_framework import serializers
from .models import *

class ArticleSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Article
        fields = ('id','title', 'description')
        



def create(self, validated_data):
    return Article.objects.create(**validated_data)


def update(self, instance, validated_data):
    instance.title = validated_data.get('title', instance.title)
    instance.description = validated_data.get('description', instance.description)
    instance.save()
    return instance