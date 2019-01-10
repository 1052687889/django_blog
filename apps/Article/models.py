from django.db import models

# Create your models here.
from datetime import datetime

from django.db import models
from DjangoUeditor.models import UEditorField

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
    content = UEditorField(verbose_name='博客内容',
                            width=700,
                            height=400,
                            toolbars='full',
                            imagePath='ueditor/images/',
                            filePath='ueditor/files/',
                            upload_settings={'imageMaxSizing':1024000},
                            default='')
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










