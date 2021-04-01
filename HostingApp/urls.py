from django.urls import path
from HostingApp import views

urlpatterns = [
    path('', views.hostingApp, name='hosting_app'),
]