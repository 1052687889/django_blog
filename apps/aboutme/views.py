from django.shortcuts import render

# Create your views here.
from django.views import View
from apps.aboutme.models import Skill,MyInfo,Level
from django.shortcuts import render_to_response
from django_blog.settings import MEDIA_URL
from apps.Article.models import Category
class About(View):
    def get(self, request):
        myinfo = MyInfo.objects.first()
        skills = Level.objects.filter(myinfo=myinfo).all()
        categorys = Category.objects.all()
        article_types = {category.id:category.name for category in categorys}
        return render_to_response('about.html',{'media':MEDIA_URL,
                                                'myinfo':myinfo,
                                                'skills':skills,
                                                'article_types': article_types
                                                })