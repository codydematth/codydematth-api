# Generated by Django 4.2 on 2024-04-15 09:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('post_title', models.CharField(max_length=255, null=True)),
                ('post_sub_title', models.CharField(max_length=255, null=True)),
                ('post_description', models.TextField(max_length=1000000, null=True)),
                ('live_url', models.CharField(blank=True, max_length=100000, null=True)),
                ('code_url', models.CharField(blank=True, max_length=100000, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='post_images/')),
                ('post_tags', models.ManyToManyField(blank=True, to='api.tag')),
            ],
        ),
    ]
