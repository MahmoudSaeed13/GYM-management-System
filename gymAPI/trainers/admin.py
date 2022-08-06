from django.contrib import admin
from trainers.models import Trainer


class TrainerAdmin(admin.ModelAdmin):
    list_display = ("name", "age", "gender", "phone", "experience", "branch_id", "class_id","created", "modified")

admin.site.register(Trainer, TrainerAdmin)
