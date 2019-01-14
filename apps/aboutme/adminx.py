#! /usr/bin/env python
# -*- coding:utf-8-*-
__author__ = "taoke"
__datetime__ = "19-1-13 11:57:39"
import xadmin
from .models import *

class MyInfoAdmin(object):
    list_display = ['zh_name','net_name','en_name','head_img','age','sex','phone','email','addr','wechat','resume','skills',]
    style_fields = {"describe": "ueditor"}

class SkillAdmin(object):
    list_display = ["name",]

class LevelAdmin(object):
    list_display = ['myinfo','skill','score']



xadmin.site.register(MyInfo, MyInfoAdmin)
xadmin.site.register(Skill, SkillAdmin)
xadmin.site.register(Level, LevelAdmin)
