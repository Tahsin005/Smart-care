# Generated by Django 4.2.10 on 2024-05-03 16:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='cancle',
            new_name='cancel',
        ),
    ]
