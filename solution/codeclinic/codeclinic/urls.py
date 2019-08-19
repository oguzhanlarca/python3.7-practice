from django.contrib import admin
from django.urls import re_path
from dashboard import views

urlpatterns = [
    re_path(r'^$', views.dashboardCurrentTime),
    re_path(r'^t=(\d{2}):(\d{2}):(\d{2})$', views.dashboardRequestTime),
]
