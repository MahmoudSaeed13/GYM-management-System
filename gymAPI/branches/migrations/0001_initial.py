# Generated by Django 4.1 on 2022-08-15 18:00

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("classes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Branch",
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
                ("name", models.CharField(max_length=150, verbose_name="Branch Name")),
                (
                    "address",
                    models.CharField(max_length=150, verbose_name="Branch Address"),
                ),
                ("description", models.TextField(verbose_name="Branch Description")),
                (
                    "phone",
                    models.CharField(
                        max_length=11, unique=True, verbose_name="branch Phone"
                    ),
                ),
            ],
            options={
                "get_latest_by": "modified",
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="BranchClass",
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
                ("appointment", models.DateTimeField(verbose_name="Class Appointment")),
                (
                    "branch_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="branches.branch",
                    ),
                ),
                (
                    "class_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="classes.class"
                    ),
                ),
            ],
            options={
                "unique_together": {("class_id", "branch_id")},
            },
        ),
    ]
