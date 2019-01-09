#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:taoke

import xadmin
from django.urls import path
from .views import category,blog,loadArticle,article,tag,_date

urlpatterns = [
    path('',blog.as_view(),name='blog'),
    path('tag/<int:_id>/',tag.as_view(),name='tag'),
    path('article/<int:_id>/',article.as_view()),
    path('date/<int:year>/<int:month>/',_date.as_view()),
    path('loadArticle/',loadArticle.as_view()),
    path('category/<int:_id>/',category.as_view()),
    path('category/<int:_id>/loadArticle/',loadArticle.as_view()),
]


