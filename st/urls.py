from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'st'
urlpatterns = [
    url(r'^$', views.drillhole, name='index'),
    url(r'^sample/(?P<id>[0-9]+)/$', views.sample, name='sample'),
    url(r'^activity/$', views.index, name='activity'),
    url(r'^log/$', views.get_log),
    url(r'^log/(?P<id>[0-9]+)/$', views.get_logentry),
]
