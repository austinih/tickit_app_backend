# Generated by Django 4.1.7 on 2023-03-31 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tickit', '0002_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='no ticket name', max_length=100)),
                ('email', models.CharField(default='no ticket email', max_length=100)),
                ('phone_number', models.CharField(default='no phone number', max_length=20)),
                ('seat_number', models.CharField(blank=True, max_length=10)),
                ('credit_card_number', models.CharField(default='0', max_length=20)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='tickit.event')),
            ],
        ),
    ]