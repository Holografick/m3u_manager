from django.contrib import admin
from . import models

class LinkInline(admin.TabularInline):
    model = models.Link

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

class ChannelAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    list_filter = ['category']
    inlines = [
        LinkInline
    ]

class LinkAdmin(admin.ModelAdmin):
    list_display = ['channel', 'url', 'is_primary']
    list_filter = ['channel__name', 'is_primary']

admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Channel, ChannelAdmin)
admin.site.register(models.Link, LinkAdmin)

