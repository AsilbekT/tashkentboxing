# Generated by Django 4.1.1 on 2022-10-03 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='image',
            field=models.ImageField(default='a.png', upload_to='static/schools_img/'),
        ),
    ]
