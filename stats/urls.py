from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^record-ping/', 'stats.views.record_ping_view'),
]
