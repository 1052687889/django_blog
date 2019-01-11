from django.shortcuts import render
from django.http.response import Http404,JsonResponse
from django.db.models import Count
from django.db.models.functions import ExtractYear,ExtractMonth
# Create your views here.

from django.views import View
from django.conf import settings
import datetime
from apps.Article.models import Article,Category,Tag
from lxml import etree
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
        read_num_article_list = Article.objects.all().order_by('-read_num')[0:5]
        try:
            context['type'] = '分类 - '+_type.name
            context['tags'] = {tag.id: [tag.name, settings.TAG_COLOR_LIST[index % len(settings.TAG_COLOR_LIST)]] for
                               index, tag in enumerate(tags)}
            context['new_article_list'] = {article.id: article.title for article in new_article_list}
            context['article_types'] = {category['category']: category['category__name'] for category in group}
            context['date'] = [(d['year'], d['month'], d['nums']) for d in _date]
            context['group'] = [(category['category'], category['category__name'], category['total']) for category in group]
            context['read_num'] = [(d.id, d.title, d.read_num) for d in read_num_article_list]
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
        read_num_article_list = Article.objects.all().order_by('-read_num')[0:5]
        context['type'] = '全部'
        context['tags'] = {tag.id:[tag.name,settings.TAG_COLOR_LIST[index % len(settings.TAG_COLOR_LIST)]] for index,tag in enumerate(tags)}
        context['new_article_list'] = {article.id:article.title for article in new_article_list}
        context['date'] = [(d['year'],d['month'],d['nums']) for d in _date]
        context['group'] = [(category['category'], category['category__name'],category['total']) for category in group]
        context['read_num'] = [(d.id,d.title,d.read_num) for d in read_num_article_list]
        return render(request, 'article_list.html',context=context)


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
        read_num_article_list = Article.objects.all().order_by('-read_num')[0:5]
        try:
            context['type'] = '标签 - '+tag.name
            context['tags'] = {tag.id: [tag.name, settings.TAG_COLOR_LIST[index % len(settings.TAG_COLOR_LIST)]] for
                               index, tag in enumerate(tags)}
            context['new_article_list'] = {article.id: article.title for article in new_article_list}
            context['article_types'] = {category['category']: category['category__name'] for category in group}
            context['date'] = [(d['year'], d['month'], d['nums']) for d in _date]
            context['group'] = [(category['category'], category['category__name'], category['total']) for category in
                                group]
            context['read_num'] = [(d.id, d.title, d.read_num) for d in read_num_article_list]
        except Exception as e:
            return render(request, '404.html', context=context)
        return render(request, 'article_list.html', context=context)

class _date(View):
    def get(self,request,year,month):
        context = {}
        new_article_list = Article.objects.order_by('create_time')[0:5]
        tags = Tag.objects.order_by('id').all()
        _date = Article.objects \
            .annotate(year=ExtractYear('create_time'), month=ExtractMonth('create_time')) \
            .values('year', 'month') \
            .annotate(nums=Count('create_time'))
        group = Article.objects.all().values('category', 'category__name').annotate(total=Count('category')).order_by(
            'total')
        read_num_article_list = Article.objects.all().order_by('-read_num')[0:5]
        try:
            context['type'] = "归档 - %s年%s月"%(year,month)
            context['tags'] = {tag.id: [tag.name, settings.TAG_COLOR_LIST[index % len(settings.TAG_COLOR_LIST)]] for
                               index, tag in enumerate(tags)}
            context['new_article_list'] = {article.id: article.title for article in new_article_list}
            context['article_types'] = {category['category']: category['category__name'] for category in group}
            context['date'] = [(d['year'], d['month'], d['nums']) for d in _date]
            context['group'] = [(category['category'], category['category__name'], category['total']) for category in
                                group]
            context['read_num'] = [(d.id, d.title, d.read_num) for d in read_num_article_list]
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
        context['title'] = article.title
        new_article_list = Article.objects.order_by('create_time')[0:5]
        tags = Tag.objects.order_by('id').all()
        _date = Article.objects \
            .annotate(year=ExtractYear('create_time'), month=ExtractMonth('create_time')) \
            .values('year', 'month') \
            .annotate(nums=Count('create_time'))
        group = Article.objects.all().values('category', 'category__name').annotate(total=Count('category')).order_by(
            'total')
        read_num_article_list = Article.objects.all().order_by('-read_num')[0:5]
        try:
            # context['type'] = "归档 - %s年%s月" % (year, month)
            context['tags'] = {tag.id: [tag.name, settings.TAG_COLOR_LIST[index % len(settings.TAG_COLOR_LIST)]] for
                               index, tag in enumerate(tags)}
            context['new_article_list'] = {article.id: article.title for article in new_article_list}
            context['article_types'] = {category['category']: category['category__name'] for category in group}
            context['date'] = [(d['year'], d['month'], d['nums']) for d in _date]
            context['group'] = [(category['category'], category['category__name'], category['total']) for category in
                                group]
            context['read_num'] = [(d.id, d.title, d.read_num) for d in read_num_article_list]
            context['author'] = article.author
            context['article_read_num'] = article.read_num
            context['create_time'] = article.create_time
            context['type'] = article.category
            context['tag'] = [tag.name for tag in article.tags.all()]
            context['content'] = article.content
        except Exception as e:
            print(e)
            return render(request, '404.html', context=context)
        print(context)
        return render(request, 'article_detail.html',context=context)

