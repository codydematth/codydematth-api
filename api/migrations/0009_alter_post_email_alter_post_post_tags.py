# Generated by Django 4.2 on 2024-04-12 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_post_code_url_alter_post_live_url_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.EmailField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_tags',
            field=models.ManyToManyField(blank=True, null=True, to='api.tag'),
        ),
    ]