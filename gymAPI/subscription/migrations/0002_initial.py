# Generated by Django 4.1 on 2022-08-18 12:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("subscription", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="subscription",
            name="user_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="subscriped_users",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
