# Generated by Django 4.1.1 on 2022-10-13 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='All_types_of_chempion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_uz', models.CharField(default='', max_length=200)),
                ('type_ru', models.CharField(default='', max_length=200)),
                ('type_en', models.CharField(default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Viloyatlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('viloyat_nomi_uz', models.CharField(max_length=200)),
                ('viloyat_nomi_ru', models.CharField(max_length=200)),
                ('viloyat_nomi_en', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Boxer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=200)),
                ('nomeri', models.CharField(max_length=200)),
                ('turar_joyi', models.CharField(max_length=200)),
                ('umumiy_janglari_soni', models.CharField(default='', max_length=200)),
                ('yutganlari', models.CharField(default='', max_length=200)),
                ('yutqazganlari', models.CharField(default='', max_length=200)),
                ('nokaut', models.CharField(default='', max_length=200)),
                ('taqdim_etish_orqali', models.CharField(default='', max_length=200)),
                ('qaror', models.CharField(default='', max_length=200)),
                ('trener_1', models.CharField(default='None', max_length=200)),
                ('trener_2', models.CharField(default='None', max_length=200)),
                ('trener_3', models.CharField(default='None', max_length=200)),
                ('trener_4', models.CharField(default='None', max_length=200)),
                ('trener_5', models.CharField(default='None', max_length=200)),
                ('boxer_rasmi', models.ImageField(upload_to='uploads/boxers/')),
                ('passport_pdf', models.FileField(upload_to='uploads/passport/')),
                ('unvoni', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='boxing_app.all_types_of_chempion')),
                ('viloyat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='boxing_app.viloyatlar')),
            ],
        ),
    ]