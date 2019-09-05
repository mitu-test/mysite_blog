from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^(?P<blog_id>[0-9]+)/$', views.detail, name='blog_detail'),
    url(r'^category/(?P<category_id>[0-9]+)/$', views.catagory, name='blog_category'),
    url(r'^tag/(?P<tag_id>[0-9]+)/$', views.tag,name='blog_tag'),
    url(r'^search/$', views.search,name='blog_search'),
    # url(r'^upload/(?P<dir_name>[^/]+)$', views.upload_image, name='upload_image'),
    url(r'^archives/(?P<year>[0-9]+)/(?P<month>[0-9]+)$', views.archives, name='blog_archives'),
    url(r'^add-comment/(?P<blog_id>[0-9]+)/$', views.add_comment, name='add_comment'),


]