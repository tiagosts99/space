# Generated by Django 4.1.7 on 2023-04-15 16:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0005_rename_public_fotografia_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='data_publicada',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]