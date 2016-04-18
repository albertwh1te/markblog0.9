# coding=utf-8
from django.conf.urls import url
import views
urlpatterns = [
    url(r'^$', views.Posts_list.as_view(), name='posts_list'),
    url(r'^(?P<pk>\d+)/$', views.Posts_detail.as_view(), name="post_detail")
    # url(r'^tags/$', views.tags_list.as_view(), name='tags_list'),
    ]
