from django.shortcuts import render
from django.http.response import Http404,JsonResponse
from django.db.models import Count
from django.db.models.functions import ExtractYear,ExtractMonth
# Create your views here.

# def category_
from django.views import View
from django.conf import settings
import datetime
from apps.Article.models import Article,Category,Tag

class category(View):
    def get(self, request,_id):
        context = {}
        _type = Category.objects.filter(id=_id).first()
        new_article_list = Article.objects.order_by('create_time')[0:5]
        tags = Tag.objects.order_by('id').all()
        _date = Article.objects\
            .annotate(year=ExtractYear('create_time'),month=ExtractMonth('create_time'))\
            .values('year','month')\
            .annotate(nums=Count('create_time'))
        group = Article.objects.all().values('category','category__name').annotate(total=Count('category')).order_by('total')
        try:
            context['type'] = _type.name
            context['tags'] = {tag.id: [tag.name, settings.TAG_COLOR_LIST[index % len(settings.TAG_COLOR_LIST)]] for
                               index, tag in enumerate(tags)}
            context['new_article_list'] = {article.id: article.title for article in new_article_list}
            context['article_types'] = {category['category']: category['category__name'] for category in group}
            context['date'] = [(d['year'], d['month'], d['nums']) for d in _date]
            context['group'] = [(category['category'], category['category__name'], category['total']) for category in group]
        except Exception as e:
            return render(request, '404.html',context=context)
        return render(request, 'article_list.html',context=context)

class blog(View):
    def get(self,request):
        context = {}
        new_article_list = Article.objects.order_by('-create_time')[0:5]
        tags = Tag.objects.order_by('id').all()
        _date = Article.objects\
            .annotate(year=ExtractYear('create_time'),month=ExtractMonth('create_time'))\
            .values('year','month')\
            .annotate(nums=Count('create_time'))
        group = Article.objects.all().values('category','category__name').annotate(total=Count('category')).order_by('total')
        context['type'] = '全部'
        context['tags'] = {tag.id:[tag.name,settings.TAG_COLOR_LIST[index % len(settings.TAG_COLOR_LIST)]] for index,tag in enumerate(tags)}
        context['new_article_list'] = {article.id:article.title for article in new_article_list}
        context['date'] = [(d['year'],d['month'],d['nums']) for d in _date]
        context['group'] = [(category['category'], category['category__name'],category['total']) for category in group]
        return render(request, 'article_list.html',context=context)

class loadArticle(View):
    @staticmethod
    def get_postCon(artivle):
        try:
            return artivle.content[0:150]
        except:
            return artivle.content

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
            # tag = int(request.GET.get('tag'))
        except Exception as e:
            context = {}
            categorys = Category.objects.all()
            context['article_types'] = {category.id: category.name for category in categorys}
            return render(request, '404.html', context=context)
        if _type == -1:
            artivle_list = Article.objects.order_by('create_time').all()[index:index+num]
        else:
            artivle_list = Article.objects.filter(category=_type).order_by('create_time').all()[index:index+num]
        data = []
        for artivle in artivle_list:
            data.append({'id':artivle.id,
                         'title':artivle.title,
                         'author':artivle.author,
                         'type':artivle.category.name,
                         'postCon':self.get_postCon(artivle),
                         'tag':[tag.name for tag in artivle.tags.all()],
                         'create_time':artivle.create_time.date()})
        return JsonResponse({'dataList':data,'time':datetime.datetime.now()})

class article(View):
    def get(self,request,**kwargs):
        return render(request, 'article_detail.html')

class tag(View):
    def get(self,request,_id):
        context = {}
        tag = Tag.objects.filter(id=_id).first()
        new_article_list = Article.objects.order_by('create_time')[0:5]
        tags = Tag.objects.order_by('id').all()
        _date = Article.objects \
            .annotate(year=ExtractYear('create_time'), month=ExtractMonth('create_time')) \
            .values('year', 'month') \
            .annotate(nums=Count('create_time'))
        group = Article.objects.all().values('category', 'category__name').annotate(total=Count('category')).order_by(
            'total')
        try:
            context['type'] = tag.name
            context['tags'] = {tag.id: [tag.name, settings.TAG_COLOR_LIST[index % len(settings.TAG_COLOR_LIST)]] for
                               index, tag in enumerate(tags)}
            context['new_article_list'] = {article.id: article.title for article in new_article_list}
            context['article_types'] = {category['category']: category['category__name'] for category in group}
            context['date'] = [(d['year'], d['month'], d['nums']) for d in _date]
            context['group'] = [(category['category'], category['category__name'], category['total']) for category in
                                group]
        except Exception as e:
            return render(request, '404.html', context=context)
        return render(request, 'article_list.html', context=context)

class _date(View):
    def get(self,request,**kwargs):
        return render(request, 'article_detail.html')


