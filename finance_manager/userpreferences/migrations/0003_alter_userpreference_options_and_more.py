# Generated by Django 4.2.13 on 2024-05-16 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userpreferences', '0002_alter_userpreference_id'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userpreference',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='userpreference',
            table='tbl_userpreferences',
        ),
    ]
