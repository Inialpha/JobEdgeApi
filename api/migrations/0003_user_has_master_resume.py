# Generated by Django 5.1.4 on 2025-01-16 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_resume_address_alter_resume_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='has_master_resume',
            field=models.BooleanField(default=False),
        ),
    ]
