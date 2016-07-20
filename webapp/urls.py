from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cars', views.cars,name='cars'),
    url(r'^manufacturer', views.manufacturer,name='manufacturer'),
    url(r'^transmission', views.transmission,name='transmission'),
    url(r'^engine', views.engine,name='engine'),
    url(r'^emissions', views.emissions,name='emissions'),
    url(r'^tows', views.tows,name='tows'),
]


