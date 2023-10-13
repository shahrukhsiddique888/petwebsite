from django.contrib import admin

# Register your models here.
from . import models

# Register your models here.

class noteAdmin(admin.ModelAdmin):
    list_display = ['title', 'text']


admin.site.register(models.petList, noteAdmin)