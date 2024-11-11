# Generated by Django 5.1.2 on 2024-11-11 21:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Comments', '0001_initial'),
        ('Posts', '0006_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='Posts.posts'),
        ),
    ]
