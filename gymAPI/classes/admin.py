from django.contrib import admin
from classes.models import Attendant, Class
# Register your models here.
class ClassAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "created", "modified")
    
admin.site.register(Class, ClassAdmin)

class AttendantAdmin(admin.ModelAdmin):
    list_display = ("attendant", "clas", "created", "modified")

admin.site.register(Attendant, AttendantAdmin)