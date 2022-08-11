# Generated by Django 4.1 on 2022-08-11 15:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("events", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="participant",
            name="participant",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="participants",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterUniqueTogether(
            name="participant",
            unique_together={("event", "participant")},
        ),
    ]
