# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, patterns
from .views import post_list

urlpatterns = patterns('',
    url('^$', post_list)
)
