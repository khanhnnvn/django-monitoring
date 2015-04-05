from __future__ import absolute_import

from django.conf.urls import patterns, url
from .views import Dashboard

urlpatterns = patterns('',
                       url(regex=r'^dashboard/$',
                           view=Dashboard.as_view(),
                           name='dashboard'),
)
