from __future__ import absolute_import

from django.conf.urls import url
from .views import Dashboard

urlpatterns = [
   url(regex=r'^dashboard/$',
       view=Dashboard.as_view(),
       name='dashboard'),
]
