# Generated by Django 4.1.1 on 2022-10-10 06:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_members'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='name',
        ),
    ]