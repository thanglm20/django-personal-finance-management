# Generated by Django 4.2.13 on 2024-05-16 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userincome', '0002_alter_userincome_options_alter_source_id_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='source',
            options={'managed': True},
        ),
        migrations.AlterModelTable(
            name='source',
            table='tbl_source',
        ),
    ]
