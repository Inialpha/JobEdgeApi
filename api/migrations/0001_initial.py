# Generated by Django 5.1.4 on 2025-01-14 20:52

import django.core.validators
import django.db.models.deletion
import django.utils.timezone
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('job_id_from_source', models.CharField(max_length=255, unique=True)),
                ('job_title', models.CharField(max_length=255)),
                ('employer_name', models.CharField(max_length=255)),
                ('employer_logo', models.URLField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('employer_website', models.URLField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('job_publisher', models.CharField(max_length=255)),
                ('job_employment_type', models.CharField(choices=[('full-time', 'Full-time'), ('part-time', 'Part-time'), ('contractor', 'Contractor')], default='full-time', max_length=20)),
                ('job_employment_types', models.JSONField(default=list)),
                ('job_apply_link', models.URLField(max_length=500, validators=[django.core.validators.URLValidator()])),
                ('job_apply_is_direct', models.BooleanField(default=False)),
                ('job_description', models.TextField()),
                ('job_is_remote', models.BooleanField(default=False)),
                ('job_location', models.CharField(max_length=255)),
                ('job_city', models.CharField(max_length=100)),
                ('job_state', models.CharField(max_length=100)),
                ('job_country', models.CharField(max_length=100)),
                ('job_benefits', models.JSONField(blank=True, default=list, null=True)),
                ('job_google_link', models.URLField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('job_salary', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('job_min_salary', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('job_max_salary', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0)])),
                ('job_qualifications', models.JSONField(default=list)),
                ('job_responsibilities', models.JSONField(default=list)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active.  Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_verified', models.BooleanField(default=False, help_text='Designates whether this user has completed the email verification process to allow login.', verbose_name='verified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('is_staff', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_url', models.URLField(blank=True, help_text='URL to the uploaded resume file', max_length=500, null=True)),
                ('text', models.TextField(help_text='Parsed text from the resume')),
                ('is_master', models.BooleanField(default=False, help_text='Indicates if this is the master resume')),
                ('keywords', models.JSONField(default=list, help_text='Keywords from the resume relevant for job searching')),
                ('name', models.CharField(help_text='Name of the user', max_length=255)),
                ('summary', models.TextField(help_text='Summary of the resume')),
                ('address', models.TextField(help_text="User's address")),
                ('email', models.EmailField(help_text="User's email address", max_length=255)),
                ('linkedin', models.URLField(help_text="User's LinkedIn profile URL", max_length=500)),
                ('phone_number', models.CharField(blank=True, help_text="User's phone number", max_length=20, null=True)),
                ('website', models.URLField(blank=True, help_text="User's personal or professional website", max_length=500, null=True)),
                ('professional_experiences', models.JSONField(default=list, help_text="User's professional experiences")),
                ('skills', models.JSONField(default=list, help_text="List of user's skills")),
                ('projects', models.JSONField(default=list, help_text="User's projects")),
                ('educations', models.JSONField(default=list, help_text="List of user's education")),
                ('languages', models.JSONField(default=list, help_text='Languages spoken by the user')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Timestamp when the resume was created')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Timestamp when the resume was last updated')),
                ('user', models.ForeignKey(help_text='User associated with the resume', on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
