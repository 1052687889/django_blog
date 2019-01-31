from django.shortcuts import render
from django.http.response import HttpResponse,JsonResponse

# Create your views here.

from django.views import View
from django.conf import settings
import datetime
from apps.Article.models import Article,Category,Tag,QuertBaseData,Comment
from lxml import etree
from apps.users.models import UserProfile
from django.template import loader

class category(View):
    def get(self, request,_id):
        context = {}
        _type = Category.objects.filter(id=_id).first()
        try:
            context['type'] = '分类 - '+_type.name
            context.update(QuertBaseData(request))
        except Exception as e:
            return render(request, '404.html',context=context)
        return render(request, 'article_list.html',context=context)

class blog(View):
    def get(self,request):
        context = {}
        context['type'] = '全部'
        context.update(QuertBaseData(request))
        return render(request, 'article_list.html',context=context)


class tag(View):
    def get(self,request,_id):
        context = {}
        tag = Tag.objects.filter(id=_id).first()
        try:
            context['type'] = '标签 - '+tag.name
            context.update(QuertBaseData(request))
        except Exception as e:
            return render(request, '404.html', context=context)
        return render(request, 'article_list.html', context=context)

class _date(View):
    def get(self,request,year,month):
        context = {}
        try:
            context['type'] = "归档 - %s年%s月"%(year,month)
            context.update(QuertBaseData(request))
        except Exception as e:
            return render(request, '404.html', context=context)
        return render(request, 'article_list.html', context=context)

class loadArticle(View):
    @staticmethod
    def get_postCon(artivle):
        html = etree.HTML(artivle.content)  # 初始化生成一个XPath解析对象
        res = html.xpath("string(.)")
        try:
            return res[0:150]
        except:
            return res

    def get(self,request,**kwargs):
        try:
            link_type=request.GET.get("link_type")
            num = int(request.GET.get("num"))
            index=int(request.GET.get('index'))
            if link_type == settings.TYPE:
                _type = int(request.GET.get("type"))
                if _type == -1:
                    artivle_list = Article.objects.order_by('create_time').all()[index:index + num]
                else:
                    artivle_list = Article.objects.filter(category=_type).order_by('create_time').all()[
                                   index:index + num]
            elif link_type == settings.TAG:
                tag = int(request.GET.get('tag'))
                artivle_list = Article.objects.filter(tags=tag).order_by('create_time').all()[
                                   index:index + num]

            elif link_type == settings.DATE:
                year=int(request.GET.get("year"))
                month=int(request.GET.get("month"))
                artivle_list = Article.objects.filter(create_time__year=year,create_time__month=month).all()[
                                   index:index + num]


        except Exception as e:
            context = {}
            categorys = Category.objects.all()
            context['article_types'] = {category.id: category.name for category in categorys}
            return render(request, '404.html', context=context)

        data = []
        for artivle in artivle_list:
            data.append({'id':artivle.id,
                         'title':artivle.title,
                         'image':settings.MEDIA_URL+str(artivle.image),
                         'author':artivle.author,
                         'type':artivle.category.name,
                         'postCon':self.get_postCon(artivle),
                         'tag':[tag.name for tag in artivle.tags.all()],
                         'read_num':artivle.read_num,
                         'create_time':artivle.create_time.date()})
        return JsonResponse({'dataList':data,'time':datetime.datetime.now()})

class article(View):
    def get(self,request,_id):
        context = {}
        article = Article.objects.filter(id=_id).first()
        context['article_id'] = article.id
        context['title'] = article.title
        comments = Comment.objects.filter(blog=article).order_by('pub').all()
        try:
            context['author'] = article.author
            context['article_read_num'] = article.read_num
            context['create_time'] = article.create_time
            context['type'] = article.category
            context['tag'] = [tag.name for tag in article.tags.all()]
            context['content'] = article.content
            context['comments'] = [(i+1,comment) for i,comment in enumerate(comments)]
            context.update(QuertBaseData(request))
            context['media_url'] = settings.MEDIA_URL
        except Exception as e:
            return render(request, '404.html', context=context)
        return render(request, 'article_detail.html',context=context)


class comment(View):
    def post(self,request):
        if request.POST:
            _id = request.POST['id']
            comment = request.POST['comment']
            art = Article.objects.filter(id=_id).first()
            user = UserProfile.objects.filter(username=request.user).first()
            if art and user:
                comm = Comment(blog=art,user=user,content=comment)
                comm.save()
                num = Comment.objects.filter(blog=art).count()
                res = loader.render_to_string("comment.html",{"comment": comm,'i':num,'media_url':settings.MEDIA_URL})
                print(comm.pub)
                print(comm.pub.strftime('%Y{y}%m{m}%d{d} %H{h}%M{f}%S{s}').format(y='年',m='月',d='日',h='时',f='分',s='秒'))
                print(comm.pub.year,comm.pub.month,comm.pub.day,comm.pub.hour,comm.pub.minute)
                return HttpResponse(res)
                # return JsonResponse({'username':user.username,
                #                      'content':comm.content,
                #                      'date':'%d年%d月%d日 %2d:%2d'%(comm.pub.year,comm.pub.month,comm.pub.day,comm.pub.hour,comm.pub.minute),#comm.pub.strftime('%Y年%m月%d日 %h:%s'),
                #                      'head_image_url':settings.MEDIA_URL+'/'+str(comm.user.image),
                #                      'zan_num':comm.zan_num,
                #                      'num':num})
        return render(request, '404.html', context={})

