# Generated by Django 3.1 on 2021-11-15 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20211018_2216'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='orders',
            options={'ordering': ('-created',)},
        ),
    ]
