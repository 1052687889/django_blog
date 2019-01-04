from django.shortcuts import render

# Create your views here.
from django.views import View
from apps.aboutme.models import Skill,MyInfo,Level
from django.shortcuts import render_to_response
from django_blog.settings import MEDIA_URL
class About(View):
    def get(self, request):
        myinfo = MyInfo.objects.first()
        skills = Level.objects.filter(myinfo=myinfo).all()
        print(skills)
        return render_to_response('about.html',{'media':MEDIA_URL,
                                                'myinfo':myinfo,
                                                'skills':skills
                                                })
        # return render(request,'about.html')