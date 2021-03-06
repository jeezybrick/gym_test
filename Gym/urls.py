"""Gym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
# from social.views import GoogleLogin

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),

    # Home view
    url(r"^$", TemplateView.as_view(
        template_name='home.html'
    ), name='home'),

    url(r'^', include('my_auth.urls')),
    url(r'^', include('api.urls')),

    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    # url(r'^rest-auth/google/$', GoogleLogin.as_view(), name='google_login'),

    # Social
    url('', include('social.apps.django_app.urls', namespace='social')),
]
