# Generated by Django 5.1.4 on 2025-01-18 08:34

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_user_has_master_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resume',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
