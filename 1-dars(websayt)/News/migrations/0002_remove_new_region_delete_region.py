# Generated by Django 5.1.2 on 2024-10-21 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('News', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='new',
            name='region',
        ),
        migrations.DeleteModel(
            name='Region',
        ),
    ]
