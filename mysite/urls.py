"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.views.static import serve
from mysite.settings import MEDIA_ROOT
from blog.feed import LatestEntriesFeed
from blog import views as blog_views
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap
from blog.models import Entry
from blog import views
from blog import upload#集成kindeditor


info_dict = {
    'queryset': Entry.objects.all(),
    'date_field': 'modified_time'
}

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='blog_index'),
    url(r'^blog/', include('blog.urls', namespace='blog', app_name='blog')),
    url(r'^uploads/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, }),
    url(r'^latest/feed/$', LatestEntriesFeed()),    #RSS订阅
    url(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^sitemap\.xml$', sitemap,{'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.6)}},
        name='django.contrib.sitemaps.views.sitemap'),       #站点地图
    url(r'^upload/(?P<dir_name>[^/]+)$', upload.upload_image, name='upload_image'), #集成kindeditor

]

