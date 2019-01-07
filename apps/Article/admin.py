from django.contrib import admin

# Register your models here.
import xadmin
from .models import Tag,Category,Article,Comment

class TagAdmin(object):
    list_display = ["name",]

class CategoryAdmin(object):
    list_display = ["name",]

class ArticleAdmin(object):
    # title = models.CharField('博客标题',max_length=100)
    # content = models.TextField('博客内容')
    # author = models.CharField('作者',max_length=30)
    # create_time = models.DateTimeField('创建时间',auto_now_add=True)
    # update_time = models.DateTimeField('更新时间',auto_now=True)
    # tags = models.ManyToManyField(Tag,verbose_name='标签')
    # category = models.ForeignKey(Category,on_delete=models.CASCADE)
    list_display = ["title","content","author","create_time","update_time","tags","category"]


class CommentAdmin(object):
    list_display = ["name",]

xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Comment, CommentAdmin)