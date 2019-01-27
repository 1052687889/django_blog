from django.shortcuts import render

# Create your views here.
from django.views import View
from apps.aboutme.models import Skill,MyInfo,Level
from django.http.response import JsonResponse
from django_blog.settings import MEDIA_URL
from apps.Article.models import Category,Article
from django.db.models import Count
from datetime import datetime
from apps.Article.models import QuertBaseData
class About(View):
    def get(self, request):
        context = {}
        myinfo = MyInfo.objects.first()
        skills = Level.objects.filter(myinfo=myinfo).all()
        group = Article.objects.all().values('category', 'category__name').annotate(total=Count('category')).order_by('total')
        context['media'] = MEDIA_URL
        context['myinfo'] = myinfo
        context['skills'] = skills
        context['group'] = [(category['category'], category['category__name'], category['total']) for category in group]
        context.update(QuertBaseData(request))
        return render(request,'about.html',    context=context)

class Zan(View):
    def get(self,request):
        myinfo = MyInfo.objects.first()
        myinfo.num += 1
        myinfo.save()
        return JsonResponse({'zan_num':myinfo.num,'time':datetime.now()})
