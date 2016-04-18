# coding=utf-8
from django.conf.urls import url
import views
urlpatterns = [
    url(r'^posts/$', views.posts_list.as_view(), name='posts_list'),
    # url(r'^tags/$', views.tags_list.as_view(), name='tags_list'),
    ]
