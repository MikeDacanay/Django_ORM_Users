from django.conf.urls import url
from . import views           # This line is new!
urlpatterns = [
  url(r'^$', views.index),
  url(r'new$', views.new),
  url(r'add$', views.add),
  url(r'(?P<idx>\d+)$', views.show),
  url(r'(?P<idx>\d+)/edit$', views.edit),
  url(r'(?P<idx>\d+)/update$', views.update)
]