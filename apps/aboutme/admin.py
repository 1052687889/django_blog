from django.contrib import admin

# Register your models here.
import xadmin
from .models import *

class MyInfoAdmin(object):
    list_display = ['zh_name','net_name','en_name','head_img','age','sex','phone','email','addr','wechat','resume','skills',]

class SkillAdmin(object):
    list_display = ["name",]

class LevelAdmin(object):
    list_display = ['myinfo','skill','score']

xadmin.site.register(MyInfo, MyInfoAdmin)
xadmin.site.register(Skill, SkillAdmin)
xadmin.site.register(Level, LevelAdmin)