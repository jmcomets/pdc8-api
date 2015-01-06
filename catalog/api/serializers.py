from rest_framework import serializers
from catalog.models import Tree, TreeGenre

class TreeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tree

class TreeGenreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TreeGenre
