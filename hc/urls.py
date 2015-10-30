from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/',    include(admin.site.urls)),
    url(r'^accounts/', include('hc.accounts.urls')),
    url(r'^',          include('hc.api.urls')),
    url(r'^',          include('hc.front.urls')),
]

urlpatterns += staticfiles_urlpatterns()
