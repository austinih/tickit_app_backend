# Generated by Django 4.1.7 on 2023-04-04 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("tickit", "0003_ticket"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="image_url",
            field=models.TextField(default="default_image_url"),
        ),
    ]
