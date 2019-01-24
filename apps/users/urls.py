#! /usr/bin/env python
# -*- coding:utf-8-*-
__author__ = "taoke"
__datetime__ = "19-1-13 19:05:24"

from django.urls import path
from .views import LoginView,RegisterView,ActiveUserView

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name='login'),
    path('active/',ActiveUserView.as_view(),name='active'),
]


