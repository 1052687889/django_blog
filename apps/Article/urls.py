#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:taoke

import xadmin
from django.urls import path
from .views import category,blog

urlpatterns = [
    path('',blog.as_view(),name='blog'),
    path('category/<int:_id>/',category.as_view()),
]


