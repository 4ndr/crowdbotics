from rest_framework import serializers
from pet.models import Cat, Dog


class CatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cat
        fields = ('name', 'birthday')

class DogSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Dog
        fields = ('name', 'birthday', 'owner')