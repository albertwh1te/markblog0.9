from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
import models
# Create your views here.


class Posts_list(ListView):
    model = models.Posts


class Posts_detail(DetailView):
    model = models.Posts
