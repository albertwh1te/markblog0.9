# coding=utf-8
from django.conf.urls import url
from django.views.generic import TemplateView
import views
urlpatterns = [
    url(r'^$', views.Posts_list.as_view(), name='posts_list'),
    url(r'^(?P<pk>\d+)/$', views.Posts_detail.as_view(), name="posts_detail"),
    url(r'^about/$', TemplateView.as_view(template_name="about.html"),name="about"),
    # url(r'^tags/$', views.tags_list.as_view(), name='tags_list'),
    ]
