# Generated by Django 4.1.1 on 2022-10-10 06:57

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_rename_body_blog_body_uz_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='body_en',
            field=tinymce.models.HTMLField(default=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='body_ru',
            field=tinymce.models.HTMLField(default=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='subtitle_en',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='subtitle_ru',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_en',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='blog',
            name='title_ru',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body_uz',
            field=tinymce.models.HTMLField(default=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='subtitle_uz',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title_uz',
            field=models.CharField(default='', max_length=300),
        ),
    ]
