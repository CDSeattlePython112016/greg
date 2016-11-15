from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^process_money$', views.process_money, name='process'),
    url(r'^reset$', views.reset, name='reset')
]
