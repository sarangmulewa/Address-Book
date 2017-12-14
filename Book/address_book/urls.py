from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^loaddata', views.dumpData, name='loaddata'),
    url(r'^getdata', views.getData, name='getdata'),
    url(r'^updatedata/(?P<id>[0-9]+)', views.updateData, name='updatedata'),
    url(r'^deletedata/(?P<id>[0-9]+)', views.deleteData, name='deletedata'),
]
