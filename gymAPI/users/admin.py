from django.contrib import admin
from users.models import User, Profile
from django.utils.translation import gettext_lazy as _    

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "name", "email", "password1", "password2"),
            },
        ),
    )
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (_("Personal info"), {"fields": ("name", "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_verified",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    list_display = ("username", "name", "email", "is_superuser", "is_verified", "created", "modified", "auth_provider")
    search_fields = ["name"]

admin.site.register(User, UserAdmin)


class ProfileAdmin(admin.ModelAdmin):
    fields =  ("user", "phone", "age", "weight", "height", "gender")
    list_display = ("user", "phone", "age", "weight", "height", "bmi", "gender", "created", "modified")

admin.site.register(Profile, ProfileAdmin)
