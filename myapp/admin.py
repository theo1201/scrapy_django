from django.contrib import admin

# Register your models here.

from .models import *

class MyAdmin(admin.ModelAdmin):
    list_display = ("title", "publishtime", "editor")
    search_fields = ("title", "editor")
    list_filter = ("editor","publishtime")
    ordering = ("publishtime",)
    # fieldsets = [
    #     (None, {'fields': ['title']}),
    #     ('editor information', {'fields': ['editor', "publishtime","content","link"], 'classes': ['title']}),
    # ]

admin.site.register(Person,MyAdmin)