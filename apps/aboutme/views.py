from django.shortcuts import render

# Create your views here.
from django.views import View
from apps.aboutme.models import Skill,MyInfo,Level
from django.shortcuts import render_to_response
from django_blog.settings import MEDIA_URL
from apps.Article.models import Category,Article
from django.db.models import Count

class About(View):
    def get(self, request):
        myinfo = MyInfo.objects.first()
        skills = Level.objects.filter(myinfo=myinfo).all()
        group = Article.objects.all().values('category', 'category__name').annotate(total=Count('category')).order_by(
            'total')
        group = [(category['category'], category['category__name'], category['total']) for category in group]
        return render_to_response('about.html',{'media':MEDIA_URL,
                                                'myinfo':myinfo,
                                                'skills':skills,
                                                'group': group
                                                })
