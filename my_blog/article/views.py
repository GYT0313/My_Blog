from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from datetime import datetime

# Create your views here.


#主页
def home(request):
    post_list = Article.objects.all() #获取全部Article 对象
    return render(request, 'home.html', {'post_list': post_list})


def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    else:
        pass
    finally:
        pass
    return render(request, 'post.html', {'post': post})

