from django.contrib import admin
from .models import Project, ChronologyEntry, Skill

# Register your models here.
admin.site.register(Project)
admin.site.register(ChronologyEntry)
admin.site.register(Skill)
