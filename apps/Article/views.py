from django.shortcuts import render

# Create your views here.

# def category_
from django.views import View
from apps.Article.models import Article,Category

class category(View):
    def get(self, request,_id):
        context = {}
        artivles = Article.objects.filter(category=_id).all()
        categorys = Category.objects.all()
        _type = Category.objects.filter(id=_id).first()
        try:
            context['article_types'] = {category.id: category.name for category in categorys}
            context['type'] = _type.name
        except Exception as e:
            return render(request, '404.html',context=context)
        return render(request, 'article_list.html',context=context)

class blog(View):
    def get(self,request):
        context = {}
        articles = Article.objects.all()
        categorys = Category.objects.all()
        context['type'] = '全部'
        context['article_types'] = {category.id: category.name for category in categorys}
        print(context)
        for article in articles:
            print(article.title)
        return render(request, 'article_list.html',context=context)

