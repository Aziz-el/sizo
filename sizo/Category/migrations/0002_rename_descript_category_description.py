# Generated by Django 5.1.2 on 2024-10-18 18:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='descript',
            new_name='description',
        ),
    ]