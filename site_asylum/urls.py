from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.http.response import HttpResponse

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'site_asylum.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', lambda req: HttpResponse(b'Asylum.su')),
    url(r'^delirium/', include('site_asylum.apps.delirium.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
