from django.contrib import admin
from .models import *


# Register your models here.

#定义Admin后台
class ArticleAdmin(admin.ModelAdmin):
    list_per_page = 10
    actions_on_top = True
    actions_on_bottom = True
    list_display = ['id', 'title', 'category', 'date_time']
    # list_filter = ['title']#根据文章名称过滤
    search_fields = ['title']#以文章名称搜索



#文章
admin.site.register(Article, ArticleAdmin)
#图片
admin.site.register(PictureOfArticle)

