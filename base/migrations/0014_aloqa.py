# Generated by Django 4.0.6 on 2022-07-28 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_asosiy_rasimlar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aloqa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manzil', models.CharField(max_length=500)),
                ('tel', models.CharField(max_length=50)),
                ('pochta', models.CharField(max_length=50)),
            ],
        ),
    ]
