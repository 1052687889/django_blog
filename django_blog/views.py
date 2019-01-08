#! /usr/bin/env python
# -*- coding:utf-8-*-
__author__ = "taoke"
__datetime__ = "18-12-30 18:22:11"

from django.views import View
from django.shortcuts import render,render_to_response

from apps.Article.models import Category

class Home(View):
    def get(self, request):
        categorys = Category.objects.all()
        article_types = {category.id:category.name for category in categorys}
        return render(request,'home.html',{'article_types':article_types})


def page_not_found(request):
    context = {}
    categorys = Category.objects.all()
    context['article_types'] = {category.id: category.name for category in categorys}
    return render(request, '404.html', context=context)