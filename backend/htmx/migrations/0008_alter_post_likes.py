# Generated by Django 5.1.6 on 2025-04-23 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("htmx", "0007_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="likes",
            field=models.PositiveIntegerField(default=0),
        ),
    ]
