# Generated by Django 4.0.6 on 2022-07-22 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rahbariyat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rahbar_rasmi', models.ImageField(upload_to='')),
                ('rahbar_nomi', models.CharField(max_length=255)),
                ('lavozimi', models.CharField(max_length=255)),
                ('tugulgan_sanasi', models.CharField(max_length=25)),
                ('tugulgan_joyi', models.CharField(max_length=255)),
                ('millati', models.CharField(max_length=25)),
                ('malumoti', models.CharField(max_length=255)),
                ('mutaxassisligi', models.CharField(max_length=255)),
                ('ish_staji', models.IntegerField()),
                ('egallab_turgan_lavozimida', models.IntegerField()),
                ('tel_raqami', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('tavfsilotlar', models.TextField(blank=True, null=True)),
                ('yutuqlari', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
