from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'st'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^log/$', views.get_log),
    url(r'^log/(?P<id>[0-9]+)/$', views.get_logentry),
    url(r'^log/add/$', views.add_logentry),
]
