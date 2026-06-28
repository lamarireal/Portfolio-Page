from django.contrib import admin
from .models import Project, ChronologyEntry

# Register your models here.
admin.site.register(Project)
admin.site.register(ChronologyEntry)
