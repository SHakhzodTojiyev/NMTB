# Generated by Django 4.0.6 on 2022-07-22 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_xodimlar_alter_rahbariyat_rahbar_rasmi'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tadbirlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_1', models.ImageField(upload_to='images/')),
                ('img_2', models.ImageField(upload_to='images/')),
                ('img_3', models.ImageField(upload_to='images/')),
                ('sarlavha', models.CharField(max_length=255)),
                ('tavsifi', models.TextField(blank=True, null=True)),
                ('yaratilish_vaqti', models.DateTimeField(auto_now_add=True)),
                ('yangilaninsh_vaqti', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]