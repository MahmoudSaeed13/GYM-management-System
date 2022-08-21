# Generated by Django 4.1 on 2022-08-21 13:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "name",
                    models.CharField(max_length=155, verbose_name="User full name"),
                ),
                (
                    "username",
                    models.CharField(
                        max_length=155, unique=True, verbose_name="Username"
                    ),
                ),
                (
                    "email",
                    models.CharField(max_length=155, unique=True, verbose_name="Email"),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False, verbose_name="Is user a superuser"
                    ),
                ),
                (
                    "is_verified",
                    models.BooleanField(
                        default=False, verbose_name="Is user verified email"
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True, verbose_name="Is user account activated"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False, verbose_name="Is user a staff member"
                    ),
                ),
                (
                    "auth_provider",
                    models.CharField(default=None, max_length=255, null=True),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "get_latest_by": "modified",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Profile",
            fields=[
                (
                    "created",
                    django_extensions.db.fields.CreationDateTimeField(
                        auto_now_add=True, verbose_name="created"
                    ),
                ),
                (
                    "modified",
                    django_extensions.db.fields.ModificationDateTimeField(
                        auto_now=True, verbose_name="modified"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        max_length=20,
                        null=True,
                        unique=True,
                        verbose_name="Phone Number",
                    ),
                ),
                ("age", models.IntegerField(null=True, verbose_name="Age")),
                (
                    "weight",
                    models.DecimalField(
                        decimal_places=2, max_digits=5, null=True, verbose_name="Weight"
                    ),
                ),
                ("height", models.IntegerField(null=True, verbose_name="Height")),
                (
                    "bmi",
                    models.DecimalField(
                        decimal_places=2,
                        max_digits=4,
                        null=True,
                        verbose_name="Body Mass Index(BMI)",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        default="users/images/default-avatar.png",
                        null=True,
                        upload_to="users/images",
                    ),
                ),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female")],
                        max_length=10,
                        null=True,
                        verbose_name="Gender",
                    ),
                ),
            ],
            options={
                "get_latest_by": "modified",
                "abstract": False,
            },
        ),
    ]
