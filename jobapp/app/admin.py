from atexit import register
from django.contrib import admin
from .models import JobPost

class JobAdmin(admin.ModelAdmin):
    list_display = ('title','date','description','salary')
    
    list_filter = ('date','salary','expiry')
    
    search_fields = ['title','description']
    
    search_help_text = "write in your query and hit enter"

    # fields = (('title','description'),'expiry',)
    # exclude = ('title',)
    
    fieldsets = (
        ('Basic information',{'fields':('title','description')
        }),
        ('Advanced information',{'classes':('collapse',),
            'fields':(('expiry','salary'),'slug')
        }),
    )

# Register your models here.
admin.site.register(JobPost,JobAdmin)

