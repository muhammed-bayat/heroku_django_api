from rest_framework import serializers
from .models import *

class ArticleSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Article
        fields = '__all__'
        



def create(self, validated_data):
    return Article.objects.create(**validated_data)


def update(self, instance, validated_data):
    instance.title = validated_data.get('title', instance.title)
    instance.description = validated_data.get('description', instance.description)
    instance.save()
    return instance



class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Material
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    experiments = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = '__all__'

    def get_experiments(self, instance):
        queryset = Experiment.objects.filter(category=instance)
        serializer = ExperimentSerializer(queryset, many=True)
        return serializer.data


class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = '__all__'


class ExperimentDetailSerializer(serializers.ModelSerializer):
    materials = MaterialSerializer(many=True)

    class Meta:
        model = Experiment
        fields = '__all__'
