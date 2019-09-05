from django.contrib import admin
from . models import Entry,Category,Tag,Comments
# Register your models here.


@admin.register(Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'visiting', 'created_time', 'modified_time', ]

    class Media:
        def __init__(self):
            pass

        js = (
            '/static/js/editor/kindeditor/kindeditor-all.js',
            '/static/js/editor/kindeditor/lang/zh_CN.js',
            '/static/js/editor/kindeditor/config.js',
        )


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name' ]


class TagAdmin(admin.ModelAdmin):
    list_display = ['name' ]

class CommentsAdmin(admin.ModelAdmin):
    list_display = ['nick', 'entry', 'email', 'comment_body', 'created_time', ]
	
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Comments, CommentsAdmin)
