from django.conf.urls import url
from . import views
from .views import graph, play_count_by_month

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^bar-graph.html/', views.graph, name = bar-graph.html/),
]


