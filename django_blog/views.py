#! /usr/bin/env python
# -*- coding:utf-8-*-
__author__ = "taoke"
__datetime__ = "18-12-30 18:22:11"

from django.views import View
from django.http import HttpResponse

class Home(View):
    def get(self, request):
        return HttpResponse('result')


