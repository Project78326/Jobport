# Generated by Django 3.0 on 2021-03-31 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapp', '0013_bookmarkjob'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
