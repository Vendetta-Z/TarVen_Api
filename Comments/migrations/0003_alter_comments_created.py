# Generated by Django 5.1.2 on 2024-11-11 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comments', '0002_alter_comments_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='created',
            field=models.DateTimeField(auto_created=True, auto_now=True),
        ),
    ]
