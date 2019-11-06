# Generated by Django 2.2.7 on 2019-11-06 12:05

from django.db import migrations
from django.core.management import call_command


def load_fixture(apps, schema_editor):
    # No, it's wrong. DON'T DO THIS!
    call_command('loaddata', 'unit.json', app_label='core')


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(load_fixture),
    ]
