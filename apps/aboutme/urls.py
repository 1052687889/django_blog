#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:taoke
import xadmin
from django.urls import path,re_path,include
from .views import About,Zan
urlpatterns = [
    path('',About.as_view(),name='about'),
    path('zan/',Zan.as_view(),name='about_zan'),
]
