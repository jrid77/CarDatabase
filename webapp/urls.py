from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^recalls', views.recalls,name='recalls'),
    url(r'^mpg', views.gasMileage,name='mpg'),
    url(r'^gasToHP', views.gasToHP,name='gasToHP'),
    url(r'^sales', views.sales,name='sales'),
    url(r'^cylVsHP', views.cylVsHP,name='cylVsHP'),
    url(r'^transmission', views.transmission,name='transmission'),
    url(r'^MostTowed', views.mostTowed,name='mostTowed'),
]


