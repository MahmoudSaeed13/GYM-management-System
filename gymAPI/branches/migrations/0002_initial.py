# Generated by Django 4.1 on 2022-08-22 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("classes", "0001_initial"),
        ("branches", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="branchclass",
            name="class_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="classes.class"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="branchclass",
            unique_together={("class_id", "branch_id")},
        ),
    ]
