# coding:utf-8
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import models
# Create your views here.


class Posts_list(ListView):
    model = models.Posts
    paginate_by = 5 
    context_object_name = 'posts'
    

class Posts_detail(DetailView):
    model = models.Posts
