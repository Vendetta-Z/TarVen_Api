# Generated by Django 5.1.2 on 2024-10-27 22:33

import Posts.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Posts', '0002_remove_posts_preview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='PostFile',
            field=models.FileField(upload_to=Posts.models.getUploadFileUrl, validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpeg', 'jpg', 'png', 'mp3', 'mp4'])]),
        ),
    ]