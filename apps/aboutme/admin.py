from django.contrib import admin

# Register your models here.
import xadmin
from .models import *

class MyInfoAdmin(object):
    list_display = ['zh_name', 'zh_name_useful',
                    'net_name', 'net_name_useful',
                    'en_name','en_name_useful',
                    'head_img', 'head_img_useful',
                    'age','age_useful',
                    'sex', 'sex_useful',
                    'phone', 'phone_useful',
                    'email', 'email_useful',
                    'addr', 'addr_useful',
                    'wechat', 'wechat_useful',
                    'describe', 'describe_useful',
                    'resume', 'resume_useful',
                    'skills',
                    ]

class SkillAdmin(object):
    list_display = ["name",]

class LevelAdmin(object):
    list_display = ['myinfo','skill','score']

xadmin.site.register(MyInfo, MyInfoAdmin)
xadmin.site.register(Skill, SkillAdmin)
xadmin.site.register(Level, LevelAdmin)