# -*- coding: utf-8 -*-

from django.contrib import admin

from real_content.models import Language, Content


class LanguageAdmin(admin.ModelAdmin):
    list_display = ['short', 'name']
    search_fields = ['short', 'name']
    
admin.site.register(Language, LanguageAdmin)


class ContentAdmin(admin.ModelAdmin):
    list_display = ['content_short', 'content_category', 'language']
    search_fields = ['content']
    list_filter = ['content_category', 'language']

admin.site.register(Content, ContentAdmin)
