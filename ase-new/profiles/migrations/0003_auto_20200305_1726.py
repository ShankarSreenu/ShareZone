# Generated by Django 3.0.2 on 2020-03-05 11:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_backgroundimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='backgroundimage',
            old_name='image',
            new_name='bg',
        ),
    ]
