from django.contrib import admin
from .models import Project, ChronologyEntry, Skill


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = (
        ('English', {
            'fields': ('title', 'description', 'tags'),
        }),
        ('Spanish', {
            'fields': ('title_es', 'description_es', 'tags_es'),
            'classes': ('collapse',),
        }),
        ('Ukrainian', {
            'fields': ('title_ua', 'description_ua', 'tags_ua'),
            'classes': ('collapse',),
        }),
        ('Project details', {
            'fields': ('image', 'link', 'pub_date'),
        }),
    )
    list_display = ('title', 'pub_date')
    search_fields = ('title', 'title_es', 'title_ua', 'description')


@admin.register(ChronologyEntry)
class ChronologyEntryAdmin(admin.ModelAdmin):
    fieldsets = (
        ('English', {
            'fields': ('title', 'description'),
        }),
        ('Spanish', {
            'fields': ('title_es', 'description_es'),
            'classes': ('collapse',),
        }),
        ('Ukrainian', {
            'fields': ('title_ua', 'description_ua'),
            'classes': ('collapse',),
        }),
        ('Entry details', {
            'fields': ('date_label', 'image', 'video_url', 'link', 'side'),
        }),
    )
    list_display = ('title', 'date_label', 'side')
    search_fields = ('title', 'title_es', 'title_ua', 'description')


admin.site.register(Skill)
