"""App_Integration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.integrate.urls')),
    url(r'^djangogold/', include('apps.djangogold.urls', namespace='gold')),
    url(r'^randomword/', include('apps.rndwordgen.urls', namespace='rand')),
    url(r'^timedisplay/', include('apps.timedisplay.urls', namespace='time')),
    url(r'^courses/', include('apps.coursesapp.urls', namespace='courses')),
    url(r'^loginreg/', include('apps.loginreg.urls', namespace='login')),

]
