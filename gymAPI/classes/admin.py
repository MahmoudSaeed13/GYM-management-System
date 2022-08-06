from django.contrib import admin
from classes.models import Class
# Register your models here.
class ClassAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "created", "modified")
    
admin.site.register(Class, ClassAdmin)