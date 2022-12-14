# Generated by Django 4.1.1 on 2022-10-05 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_blog_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=200)),
                ('number', models.CharField(max_length=200)),
                ('image', models.ImageField(default='member.png', upload_to='static/members/')),
            ],
        ),
    ]
