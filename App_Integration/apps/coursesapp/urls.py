from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add$', views.add, name='add'),
    url(r'^usertocourse/$', views.add_to_course, name='usertocourse'),
    url(r'^remove/(?P<id>\d+)$', views.remove, name='remove'),
    url(r'^remove/delete/(?P<id>\d+)$', views.delete, name='delete'),
]
