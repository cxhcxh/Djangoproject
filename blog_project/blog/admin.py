# coding:utf-8
from django.contrib import admin
from models import *


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'id', 'content', 'is_recommend',
                    'date_publish', 'category', 'user')
    # fields = ('title', 'desc',  'content', 'is_recommend',
    #           'category', 'user')
    list_editable = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'desc', 'content', 'user', 'category', 'tag',)
        }),
        ('高级设置', {
            'classes': ('collapse',),
            'fields': ('click_count', 'is_recommend',)
        }),
    )

    class Media:
        def __init__(self):
            pass

        js = (
            '/static/js/kindeditor-4.1.10/kindeditor-min.js',
            '/static/js/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/js/kindeditor-4.1.10/config.js',
        )


admin.site.register(User)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Ad)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Links)
