# Generated by Django 5.0.4 on 2024-05-13 05:39

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_post_last_viewed_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='last_viewed_datetime',
            field=models.DateTimeField(default=datetime.datetime(2024, 5, 13, 5, 39, 58, 690247)),
        ),
    ]
