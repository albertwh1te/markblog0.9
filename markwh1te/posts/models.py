# coding=utf-8
from django.db import models
from django.contrib.auth.models import User


class Tags(models.Model):
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    name = models.CharField(max_length=30, verbose_name='标签名称')
        
    class Meta:
        verbose_name = '标签'
    
    def __unicode__(self):
        return self.name


class Posts(models.Model):
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    auther = models.ForeignKey(User, verbose_name='作者')
    tag = models.ManyToManyField(Tags, verbose_name='标签')
    title = models.CharField(max_length=50, verbose_name='标题')
    content = models.TextField()
    
    class Meta:
        verbose_name = '文章'
        ordering = ['-id']
    
    def __unicode__(self):
        return self.title
