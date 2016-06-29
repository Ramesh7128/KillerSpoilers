from django.conf.urls import url
from killerapp import views


urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^subscribe/$', views.subscribe, name='susbscribe'),
    ]