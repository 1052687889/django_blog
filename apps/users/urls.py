#! /usr/bin/env python
# -*- coding:utf-8-*-
__author__ = "taoke"
__datetime__ = "19-1-13 19:05:24"

from django.urls import path
from .views import register,user_login

urlpatterns = [
    path('register/',register.as_view(),name='register'),
    path('login/',user_login.as_view(),name='login'),
]


