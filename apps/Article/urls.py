#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:taoke

import xadmin
from django.urls import path
from .views import category,blog,loadArticle,article,tag,_date,comment,comment_zan

urlpatterns = [
    path('',blog.as_view(),name='blog'),
    path('tag/<int:_id>/',tag.as_view(),name='tag'),
    path('article/<int:_id>/',article.as_view()),
    # http://127.0.0.1:8000/blog/article/10/comment/zan?comment_id=71&zan_num=0&article_id=10
    path('article/<int:_id>/comment/zan',comment_zan.as_view()),
    path('date/<int:year>/<int:month>/',_date.as_view()),
    path('loadArticle/',loadArticle.as_view()),
    path('category/<int:_id>/',category.as_view()),
    path('category/<int:_id>/loadArticle/',loadArticle.as_view()),
    path('tag/<int:_id>/loadArticle/',loadArticle.as_view()),
    path('date/<int:year>/<int:month>/loadArticle/', loadArticle.as_view()),
    path('comment/',comment.as_view()),
]


