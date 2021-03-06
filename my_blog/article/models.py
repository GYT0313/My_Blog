from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField

# Create your models here.


class Article(models.Model):
    title = models.CharField('文章名称', max_length=100) #博客题目
    category = models.CharField('类别', max_length=50, blank=True) #博客标签
    date_time = models.DateTimeField('发表时间', auto_now_add=True) #博客日期
    content = HTMLField('内容', blank=True, null=True) #博客文章正文
    

    #获取URL并转换成url的表示格式
    def get_absolute_url(self):
        path = reverse('detail', kwargs={'id':self.id})
        return "http://127.0.0.1:8000%s" % path


    def __str__(self):
        return self.title

    class Meta: #按时间下降排序
        ordering = ['-date_time']


class PictureOfArticle(models.Model):
    pic = models.ImageField(upload_to = 'article/')


#富文本编辑器