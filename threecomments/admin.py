# coding: utf-8
from django.contrib import admin

from threecomments.models import Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'comment',)
    search_fields = ('comment',)
    ordering = ('-created_at',)
    readonly_fields = ('parent',)


admin.site.register(Comment, CommentAdmin)
