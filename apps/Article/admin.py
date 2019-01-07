from django.contrib import admin

# Register your models here.
import xadmin
from .models import Tag,Category,Article,Comment

class TagAdmin(object):
    list_display = ["name",]

class CategoryAdmin(object):
    list_display = ["name",]

class ArticleAdmin(object):
    list_display = ["title","author","create_time","update_time","tags","category"]


class CommentAdmin(object):
    list_display = ["name",]

xadmin.site.register(Tag, TagAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Comment, CommentAdmin)