# Generated by Django 4.0.5 on 2022-06-26 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0007_city_unit_adminuser'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='adminuser',
            name='Admin_City',
        ),
    ]
