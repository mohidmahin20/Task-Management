# Generated by Django 4.2.9 on 2024-06-28 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='task',
        ),
    ]
