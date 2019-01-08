from django.shortcuts import render
from django.http.response import Http404,JsonResponse
# Create your views here.

# def category_
from django.views import View
from django.conf import settings
import datetime
from apps.Article.models import Article,Category,Tag

class category(View):
    def get(self, request,_id):
        context = {}
        categorys = Category.objects.all()
        _type = Category.objects.filter(id=_id).first()
        new_article_list = Article.objects.order_by('create_time')[0:5]
        try:
            context['new_article_list'] = {article.id: article.title for article in new_article_list}
            context['article_types'] = {category.id: category.name for category in categorys}
            context['type'] = _type.name
        except Exception as e:
            return render(request, '404.html',context=context)
        return render(request, 'article_list.html',context=context)

class blog(View):
    def get(self,request):
        context = {}
        categorys = Category.objects.all()
        new_article_list = Article.objects.order_by('-create_time')[0:5]
        tags = Tag.objects.order_by('id').all()
        context['type'] = '全部'
        context['tags'] = {tag.id:[tag.name,settings.TAG_COLOR_LIST[index % len(settings.TAG_COLOR_LIST)]] for index,tag in enumerate(tags)}
        context['article_types'] = {category.id: category.name for category in categorys}
        context['new_article_list'] = {article.id:article.title for article in new_article_list}
        return render(request, 'article_list.html',context=context)

class loadArticle(View):
    def get(self,request,**kwargs):
        '''
        id:文章id
        title:标题
        author:作者
        tag:标签
        type:类型
        create_time:创建时间
        '''
        try:
            num = int(request.GET.get("num"))
            _type = int(request.GET.get("type"))
            index=int(request.GET.get('index'))
        except Exception as e:
            context = {}
            categorys = Category.objects.all()
            context['article_types'] = {category.id: category.name for category in categorys}
            return render(request, '404.html', context=context)
        if _type == -1:
            artivle_list = Article.objects.order_by('create_time').all()[index:num]
        else:
            artivle_list = Article.objects.filter(category=_type).order_by('create_time').all()[index:num]
        data = []
        for artivle in artivle_list:
            data.append({'id':artivle.id,
                         'title':artivle.title,
                         'author':artivle.author,
                         'type':artivle.category.name,
                         'tag':[tag.name for tag in artivle.tags.all()],
                         'create_time':artivle.create_time.date()})
        return JsonResponse({'dataList':data,'time':datetime.datetime.now()})

class article(View):
    def get(self,request,**kwargs):
        return render(request, 'article_detail.html')

class tag(View):
    def get(self,request,**kwargs):
        return render(request, 'article_detail.html')




