from django.conf.urls import patterns, include, url
from checkIn import views
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^chkIn/$', views.chkIn),
		url(r'^attendance/$', views.showAttendance),
)
