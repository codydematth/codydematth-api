# Generated by Django 4.2 on 2024-04-12 02:04

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_alter_post_post_sub_title_alter_post_post_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_tags',
        ),
        migrations.AddField(
            model_name='post',
            name='post_tags',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name=api.models.Tag),
        ),
    ]
