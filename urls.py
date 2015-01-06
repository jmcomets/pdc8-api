from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
        # Catalog API
        url(r'^api/', include('catalog.urls')),

        # Admin site
        url(r'^admin/', include(admin.site.urls)),
        )
