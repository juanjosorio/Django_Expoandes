# Generated by Django 3.1.2 on 2020-11-27 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='audio_file',
            field=models.FileField(blank=True, default='', null=True, upload_to='canciones'),
        ),
    ]
