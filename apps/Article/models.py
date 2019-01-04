from django.db import models

# Create your models here.
from datetime import datetime

from django.db import models

class Tag(models.Model):
    '''
    博客标签
    '''
    name = models.CharField('名称',max_length=16)
    class Meta:
        verbose_name='标签'
        verbose_name_plural = verbose_name

class Category(models.Model):
    """
    博客分类
    """
    name=models.CharField('名称',max_length=30)
    class Meta:
        verbose_name="类别"
        verbose_name_plural=verbose_name



class Article(models.Model):
    '''
    博客文章
    '''
    title = models.CharField('博客标题',max_length=100)
    content = models.TextField('博客内容')
    author = models.CharField('作者',max_length=30)
    create_time = models.DateTimeField('创建时间',auto_now_add=True)
    update_time = models.DateTimeField('更新时间',auto_now=True)
    tags = models.ManyToManyField(Tag,verbose_name='标签')
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    class Meta:
        verbose_name="博客"
        verbose_name_plural=verbose_name


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










