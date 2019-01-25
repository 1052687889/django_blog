#! /usr/bin/env python
# -*- coding:utf-8-*-
__author__ = "taoke"
__datetime__ = "18-12-30 18:22:11"

from django.views import View
from django.shortcuts import render

from django_blog.genfunc import get_top_data

class Home(View):
    def get(self, request):
        context = get_top_data(request)
        return render(request,'home.html',context)


def page_not_found(request):
    context = get_top_data(request)
    return render(request, '404.html', context=context)















