# Generated by Django 3.1.1 on 2020-09-30 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0006_auto_20200930_2004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='export_csv',
        ),
    ]
