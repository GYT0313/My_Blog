"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from article import views
from article.views import RSSFeed


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^$', views.home, name='home'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^archives/$', views.archives, name='archives'),
    url(r'^aboutme/$', views.about_me, name='about_me'),
    url(r'^tag(?P<tag>\w+)/$', views.search_tag, name='search_tag'),
    url(r'^search/$', views.blog_search, name='search'),
    url(r'^feed/$', RSSFeed(), name='RSS') #新添加的urlconf,并将name设置为RSS, 方便在模板中使用url
]
