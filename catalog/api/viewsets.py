from rest_framework import viewsets
from catalog.api.serializers import TreeSerializer, TreeGenreSerializer
from catalog.models import Tree, TreeGenre

class TreeViewSet(viewsets.ModelViewSet):
    serializer_class = TreeSerializer
    queryset = Tree.objects.all()

class TreeGenreViewSet(viewsets.ModelViewSet):
    serializer_class = TreeGenreSerializer
    queryset = TreeGenre.objects.all()
