# Generated by Django 4.1 on 2023-03-20 07:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("monitor", "0001_initial"),
        ("detect", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="DetectResult",
            new_name="Detect",
        ),
    ]