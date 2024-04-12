# Generated by Django 4.2 on 2024-04-12 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_tag_post_image_post_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='code_url',
            field=models.CharField(blank=True, max_length=100000, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='live_url',
            field=models.CharField(blank=True, max_length=100000, null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
