# Generated by Django 5.1 on 2024-09-13 06:19

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docs', '0005_remove_documents_users'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='users',
            field=models.ManyToManyField(related_name='documents', through='docs.DocumentsPermissions', to=settings.AUTH_USER_MODEL),
        ),
    ]
