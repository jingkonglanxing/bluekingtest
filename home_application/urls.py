# -*- coding: utf-8 -*-

from django.conf.urls import patterns
from views import index,add

urlpatterns = patterns('home_application.views',
    (r'^$', 'index'),
    (r'add/$','add'),
    (r'^dev-guide/$', 'dev_guide'),
    (r'^contactus/$', 'contactus'),
)

