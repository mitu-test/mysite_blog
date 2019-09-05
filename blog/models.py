from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    """
    博客分类
    """
    name = models.CharField(max_length=128,verbose_name='博客分类')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '博客分类'
        verbose_name_plural = '博客分类'


class Tag(models.Model):
    """
    博客标签
    """
    name = models.CharField(max_length=128,verbose_name='博客标签')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '博客标签'
        verbose_name_plural = '博客标签'


class Entry(models.Model):
    """
    博客详情
    """
    title = models.CharField(max_length=128,verbose_name='文章标题')
    author = models.ForeignKey(User,verbose_name='博客作者')
    img = models.ImageField(upload_to='blog_image/%Y%m',null=True,blank=True,verbose_name='博客配图')
    body = models.TextField(verbose_name='博客正文')
    resource_name = models.CharField(max_length=100, verbose_name="资料名称",null=True,blank=True,)
    download = models.FileField(upload_to="resource/%Y%m", verbose_name="资源文件", max_length=100,null=True,blank=True,)
    abstract = models.TextField(max_length=256,blank=True,null=True,verbose_name='博客摘要')
    visiting = models.PositiveIntegerField(default=0,verbose_name='博客访问量')
    category = models.ForeignKey(Category,verbose_name='博客分类')
    tags = models.ForeignKey(Tag,verbose_name='博客标签',null=True,blank=True)
    created_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    modified_time = models.DateTimeField(auto_now=True,verbose_name='修改时间')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # 获取当前博客详情页的url
        return reverse("blog:blog_detail", kwargs={"blog_id": self.id})  # app名字，详情页url的别名，参数是当前博客的id

    def increase_visiting(self):
        # 访问量加1
        self.visiting += 1
        self.save(update_fields=['visiting'])  # 只保存某个字段

    def get_comment_count(self):
        #获取评论数
        return self.comments_set.all().count()

    class Meta:
        ordering = ['-created_time']
        verbose_name = '博客'
        verbose_name_plural = '博客'


class Comments(models.Model):
    """评论"""
    nick = models.CharField(max_length=20,verbose_name="昵称")
    entry = models.ForeignKey(Entry,verbose_name="博客")
    email = models.EmailField(verbose_name="邮箱")
    comment_body = models.TextField(verbose_name="评论",max_length=200)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        ordering = ['-created_time']
        verbose_name = '博客评论'
        verbose_name_plural = '博客评论'
