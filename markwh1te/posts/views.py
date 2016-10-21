# coding:utf-8
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import models
# Create your views here.


class Posts_list(ListView):
    models = models.Posts
    paginate_by = 5
    context_object_name = 'posts'

    def get_queryset(self):
        print self.request.GET.get('keyword',None)
        keyword = self.request.GET.get('keyword', None)
        if keyword:
            object_list = self.models.objects.filter(title__contains=keyword)
        else:
            object_list = self.models.objects.all()
        return object_list


class Posts_detail(DetailView):
    model = models.Posts


class Archieve(ListView):
    model = models.Posts
    paginate_by = 20
    context_object_name = 'posts'
    template_name = 'posts/archieve.html'
