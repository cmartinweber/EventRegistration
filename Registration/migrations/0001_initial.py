# Generated by Django 5.1.4 on 2025-02-02 04:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('session_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100)),
                ('email_address', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=14)),
                ('dietary_preferences', models.CharField(blank=True, max_length=500)),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Registration.session')),
            ],
        ),
    ]
