from django import template
from ..models import Entry,Category,Tag

register = template.Library()


@register.simple_tag
#获取博客数量
def get_entries():
    return Entry.objects.all().count()


@register.simple_tag
#获取最热博客
def get_popular_entries(num=5):
    return Entry.objects.all().order_by('-visiting')[:num]


@register.simple_tag
#获取博客分类数
def get_categories():
    return Category.objects.all()


@register.simple_tag
#每一分类的博客数
def get_entry_count_of_category(category_name):
    return Entry.objects.filter(category__name=category_name).count()


@register.simple_tag
#博客归档
def archives():
    return Entry.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
#博客按日期归档
def get_entry_count_of_date(year, month):
    return Entry.objects.filter(created_time__year=year, created_time__month=month).count()


@register.simple_tag
#获取标签数
def get_tags():
    return Tag.objects.all()


@register.simple_tag
#每一标签的博客数
def get_entry_count_of_tag(tag_name):
    return Entry.objects.filter(tags__name=tag_name).count()

