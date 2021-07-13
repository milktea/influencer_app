"""influencer_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import include, path

API_PREFIX = 'api'

urlpatterns = [
    path(f'{API_PREFIX}/campaigns/', include('campaigns.urls')),
    path('admin/', admin.site.urls),
]
