# Generated by Django 5.0.6 on 2024-08-01 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_follow_profile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]