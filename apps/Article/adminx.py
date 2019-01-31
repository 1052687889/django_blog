#! /usr/bin/env python
# -*- coding:utf-8-*-
__author__ = "taoke"
__datetime__ = "19-1-13 11:57:57"
import xadmin
from .models import Tag,Category,Article,Comment

class TagAdmin(object):
    list_display = ["name",]

class CategoryAdmin(object):
    list_display = ["name",]

class ArticleAdmin(object):
    list_display = ["title","author","category","tags","read_num","create_time","update_time"]
    # style_fields = {"content": "ueditor"}


class CommentAdmin(object):
    # blog=models.ForeignKey(Article,verbose_name='博客',on_delete=models.DO_NOTHING)#(博客--评论:一对多)
    # user=models.ForeignKey(UserProfile,verbose_name='用户',on_delete=models.DO_NOTHING)
    # content=models.CharField('内容',max_length=240)
    # pub=models.DateField('发布时间',auto_now_add=True)
    list_display = ["blog","user","content","pub"]

xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Comment, CommentAdmin)
