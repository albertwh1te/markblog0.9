from django.shortcuts import render
from django.views.generic.list import ListView
import models
# Create your views here.


class posts_list(ListView):
    model = models.Posts
