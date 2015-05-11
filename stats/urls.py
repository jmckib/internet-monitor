from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'stats.views.index_view'),
    url(r'^record-ping/', 'stats.views.record_ping_view'),
    url(r'^record-speed/', 'stats.views.record_speed_view'),
]
