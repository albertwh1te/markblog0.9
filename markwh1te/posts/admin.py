# coding=utf-8
from django.contrib import admin
from models import Posts, Tags
from django.db import models
from pagedown.widgets import AdminPagedownWidget
# Register your models here.

admin.site.register(Tags)


class PostsAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminPagedownWidget},
    }
    
    class Meta:
        model = Posts


admin.site.register(Posts, PostsAdmin)
