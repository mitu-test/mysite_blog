from django.shortcuts import render,reverse,redirect
from . import models
# import markdown,pygments
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm
from django.db.models import Q
# Create your views here.


def index(request):
    """
    主页视图
    """
    entries = models.Entry.objects.all()
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(entries, 6, request=request)
    entry_list = p.page(page)

    return render(request,'blog/index.html',locals())


def detail(request,blog_id):
    """
    博客详情
    """
    entry = models.Entry.objects.get(id=blog_id)
    all_comments = models.Comments.objects.all()
    comment_count = models.Comments.objects.all().count()
    # md = markdown.Markdown(extensions=[
    #     'markdown.extensions.extra',
    #     'markdown.extensions.codehilite',
    # ])
    # entry.body = md.convert(entry.body)
    entry.increase_visiting()
    return render(request,'blog/detail.html',locals())


def search(request):
    """博客搜索"""
    keyword = request.GET.get('keyword', None)
    entries = models.Entry.objects.filter(Q(title__icontains=keyword)
                                          | Q(body__icontains=keyword)
                                          | Q(abstract__icontains=keyword))
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(entries, 6, request=request)
    entry_list = p.page(page)
    return render(request, 'blog/index.html', locals())


def catagory(request,category_id):
    """
    博客分类
    """
    c = models.Category.objects.get(id=category_id)
    entries = models.Entry.objects.filter(category=c)
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(entries, 6, request=request)
    entry_list = p.page(page)

    return render(request, 'blog/index.html', locals())


def tag(request,tag_id):
    """标签"""
    t = models.Tag.objects.get(id=tag_id)
    if t.name == "全部":
        entries = models.Entry.objects.all()
    else:
        entries = models.Entry.objects.filter(tags=t)
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(entries, 6, request=request)
    entry_list = p.page(page)

    return render(request, 'blog/index.html', locals())


def add_comment(request,blog_id):
    """
    添加博客评论
    """
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            nick = request.POST.get("nick","")
            email = request.POST.get("email","")
            comment_body = request.POST.get("comment_body","")
            entry = models.Entry.objects.get(id=int(blog_id))
            new_comment = models.Comments()
            new_comment.nick = nick
            new_comment.email = email
            new_comment.comment_body = comment_body
            new_comment.entry = entry
            new_comment.save()
    return redirect(reverse("blog:blog_detail",kwargs={'blog_id':blog_id}))


def archives(request, year, month):
    """归档"""

    entries = models.Entry.objects.filter(created_time__year=year, created_time__month=month)
    try:
        page = request.GET.get('page', 1)
    except PageNotAnInteger:
        page = 1
    p = Paginator(entries, 6, request=request)
    entry_list = p.page(page)
    return render(request, 'blog/index.html', locals())


