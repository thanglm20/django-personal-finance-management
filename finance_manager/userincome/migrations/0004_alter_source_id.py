# Generated by Django 4.2.13 on 2024-05-17 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userincome', '0003_alter_source_options_alter_source_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='source',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
