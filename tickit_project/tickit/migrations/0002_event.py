# Generated by Django 4.1.7 on 2023-03-31 16:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickit', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='no event title', max_length=100)),
                ('artist', models.CharField(default='no artist title', max_length=100)),
                ('date', models.DateField(null=True)),
                ('genre', models.CharField(default='no genre title', max_length=100)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='tickit.venue')),
            ],
        ),
    ]
