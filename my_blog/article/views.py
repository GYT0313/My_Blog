from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from datetime import datetime

# Create your views here.


#主页
def home(request):
    post_list = Article.objects.all() #获取全部Article 对象
    return render(request, 'home.html', {'post_list': post_list})


def detail(request, my_args):
    post = Article.objects.all()[int(my_args)]
    str = ("title = %s, category = %s, data_time = %s, content = %s"%(post.title, post.category, post.date_time, post.content))
    return HttpResponse(str)

