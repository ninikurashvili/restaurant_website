# Generated by Django 4.2.20 on 2025-03-20 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_location_alter_customuser_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='location',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='phone',
            field=models.CharField(default='0000000000', max_length=15),
            preserve_default=False,
        ),
    ]
