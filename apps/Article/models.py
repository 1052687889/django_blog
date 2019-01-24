from django.db import models

# Create your models here.
from datetime import datetime
from django.db.models import Count
from django.db import models
from django.db.models import Count
from django.db.models.functions import ExtractYear,ExtractMonth
from django.conf import settings
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Tag(models.Model):
    '''
    博客标签
    '''
    name = models.CharField('名称',max_length=16)
    class Meta:
        verbose_name='标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class Category(models.Model):
    """
    博客分类
    """
    name=models.CharField('名称',max_length=30)
    class Meta:
        verbose_name="类别"
        verbose_name_plural=verbose_name

    def __str__(self):
        return self.name



class Article(models.Model):
    '''
    博客文章
    '''
    title = models.CharField('博客标题',max_length=100)
    # content = models.TextField('博客内容')
    content = RichTextUploadingField(verbose_name='博客内容')
    image = models.ImageField('文章图片', upload_to='img/%Y/%m/%d', null=False, default='/default/head.jpg')
    author = models.CharField('作者',max_length=30)
    # create_time = models.DateTimeField('创建时间',auto_now_add=True)
    create_time = models.DateTimeField('创建时间')
    update_time = models.DateTimeField('更新时间',auto_now=True)
    tags = models.ManyToManyField(Tag,verbose_name='标签')
    category = models.ForeignKey(Category,verbose_name='分类',on_delete=models.CASCADE)
    read_num = models.IntegerField('阅读数',default=0)

    class Meta:
        verbose_name="博客"
        verbose_name_plural=verbose_name

    @staticmethod
    def get_group():
        context = {}
        group = Article.objects.all().values('category', 'category__name').annotate(total=Count('category')).order_by(
            'total')
        context['group'] = [(category['category'], category['category__name'], category['total']) for category in group]
        return context

    def __str__(self):
        return self.title

class Comment(models.Model):
    '''
    博客评论
    '''
    blog=models.ForeignKey(Article,verbose_name='博客',on_delete=models.DO_NOTHING)#(博客--评论:一对多)
    name=models.CharField('称呼',max_length=16)
    email=models.EmailField('邮箱')
    content=models.CharField('内容',max_length=240)
    pub=models.DateField('发布时间',auto_now_add=True)

    class Meta:
        verbose_name="评论"
        verbose_name_plural="评论"

    def __str__(self):
        return self.name + ':' + self.name




from django_blog.genfunc import get_top_data

def QuertBaseData(request):
    '''
    查询博客基本信息
    :return:
    '''
    context = get_top_data(request)
    new_article_list = Article.objects.order_by('create_time')[0:5]
    tags = Tag.objects.order_by('id').all()
    _date = Article.objects.annotate(year=ExtractYear('create_time'), month=ExtractMonth('create_time')).values('year', 'month').annotate(nums=Count('create_time'))
    group = Article.objects.all().values('category', 'category__name').annotate(total=Count('category')).order_by('total')
    read_num_article_list = Article.objects.all().order_by('-read_num')[0:5]
    context['tags'] = {tag.id: [tag.name, settings.TAG_COLOR_LIST[index % len(settings.TAG_COLOR_LIST)]] for index, tag in enumerate(tags)}
    context['new_article_list'] = {article.id: article.title for article in new_article_list}
    context['article_types'] = {category['category']: category['category__name'] for category in group}
    context['date'] = [(d['year'], d['month'], d['nums']) for d in _date]
    context['group'] = [(category['category'], category['category__name'], category['total']) for category in group]
    context['read_num'] = [(d.id, d.title, d.read_num) for d in read_num_article_list]
    return context



