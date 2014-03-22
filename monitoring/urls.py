from __future__ import absolute_import

from django.conf.urls import patterns, url
from .views import dashboard

urlpatterns = patterns('',
    url(regex=r'^dashboard/$',
        view=dashboard,
        name='dashboard'),
)
