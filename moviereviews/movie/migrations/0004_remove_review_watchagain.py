# Generated by Django 5.1 on 2024-09-07 14:16

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("movie", "0003_rename_watchagain_review_watchagain"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="review",
            name="watchAgain",
        ),
    ]
