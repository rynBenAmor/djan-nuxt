# Generated by Django 5.1.6 on 2025-02-22 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_comment_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(choices=[('Tunis', 'Tunis'), ('Paris', 'Paris'), ('New York', 'New York'), ('Tokyo', 'Tokyo'), ('Cairo', 'Cairo')], max_length=50)),
            ],
        ),
    ]
