# Generated by Django 4.1.7 on 2023-04-04 15:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickit', '0004_event_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='image_url',
        ),
    ]