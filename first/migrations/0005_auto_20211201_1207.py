# Generated by Django 3.2.2 on 2021-12-01 09:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0004_auto_20211201_1156'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='title_tag',
        ),
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]
