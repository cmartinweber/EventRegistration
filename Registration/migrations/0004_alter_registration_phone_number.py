# Generated by Django 5.1.4 on 2025-02-02 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration', '0003_alter_registration_email_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='phone_number',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
