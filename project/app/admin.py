from django.contrib import admin
from .models import classes,employee,Students
# Register your models here.
 
 
 #for string method 
# admin.site.register(classes) 

# for list method 

class classadmin(admin.ModelAdmin):
    list_display=('firstname','lastname','age',)
admin.site.register(classes,classadmin)
admin.site.register(employee) 
admin.site.register(Students)   


