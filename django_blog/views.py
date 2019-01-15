#! /usr/bin/env python
# -*- coding:utf-8-*-
__author__ = "taoke"
__datetime__ = "18-12-30 18:22:11"

from django.views import View
from django.shortcuts import render

from apps.Article.models import Category,Article
from django.db.models import Count
class Home(View):
    def get(self, request):
        context = {}
        group = Article.objects.all().values('category', 'category__name').annotate(total=Count('category')).order_by(
            'total')
        context['group'] = [(category['category'], category['category__name'], category['total']) for category in group]
        return render(request,'home.html',context)


def page_not_found(request):
    context = {}
    group = Article.objects.all().values('category', 'category__name').annotate(total=Count('category')).order_by(
        'total')
    context['group'] = [(category['category'], category['category__name'], category['total']) for category in group]
    return render(request, '404.html', context=context)















