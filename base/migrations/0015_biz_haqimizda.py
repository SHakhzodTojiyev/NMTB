# Generated by Django 4.0.6 on 2022-07-28 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_aloqa'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biz_haqimizda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('biz_haqimizda', models.TextField()),
            ],
        ),
    ]