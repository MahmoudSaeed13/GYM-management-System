from django.contrib import admin
from branches.models import Branch, BranchClass


# Register your models here.
class BranchAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "description", "phone", "created", "modified")

admin.site.register(Branch, BranchAdmin)



class BranchClassAdmin(admin.ModelAdmin):
    list_display = ("class_id", "branch_id", "appointment", "created", "modified")

admin.site.register(BranchClass, BranchClassAdmin)