from django.conf.urls import patterns, include, url
from catalog.api.viewsets import TreeViewSet, TreeGenreViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'trees', TreeViewSet)
router.register(r'tree_genres', TreeGenreViewSet)

urlpatterns = patterns('',
    # Wire up our API using automatic URL routing.
    # Additionally, we include login URLs for the browsable API.
    url(r'^', include(router.urls)),
    # API authentication
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
    )
