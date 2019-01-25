#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:taoke
from apps.Article.models import Article
from apps.users.models import UserProfile
from django.conf import settings
def get_top_data(request):
    context = {}
    context.update(Article.get_group())
    user = UserProfile.objects.filter(username=request.user).first()
    if user:
        context['head_image'] = settings.MEDIA_URL + str(user.image)
        context['username'] = user.username
    return context






