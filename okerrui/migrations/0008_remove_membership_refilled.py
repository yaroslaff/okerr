# Generated by Django 3.0.2 on 2020-02-25 14:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('okerrui', '0007_remove_profilearg_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='membership',
            name='refilled',
        ),
    ]
