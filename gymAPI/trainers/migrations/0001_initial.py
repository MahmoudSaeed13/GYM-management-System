# Generated by Django 4.1 on 2022-08-20 21:42

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("classes", "0001_initial"),
        ("branches", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Trainer",
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
                ("name", models.CharField(max_length=150, verbose_name="Trainer Name")),
                ("age", models.IntegerField(verbose_name="Trainer Age")),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "Male"), ("female", "Female")],
                        default="male",
                        max_length=6,
                        verbose_name="Trainer Gener",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        max_length=11, unique=True, verbose_name="TRainer Phone number"
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        default="users/images/default-avatar.png",
                        upload_to="user/images",
                        verbose_name="Trianer personal Image",
                    ),
                ),
                (
                    "experience",
                    models.IntegerField(verbose_name="Trainer years of experince"),
                ),
                (
                    "branch_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="branches",
                        to="branches.branch",
                    ),
                ),
                (
                    "class_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="classes",
                        to="classes.class",
                    ),
                ),
            ],
            options={
                "get_latest_by": "modified",
                "abstract": False,
            },
        ),
    ]
