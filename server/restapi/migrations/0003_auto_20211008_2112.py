# Generated by Django 3.2.7 on 2021-10-09 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0002_auto_20211005_2103'),
    ]

    operations = [
        migrations.AddField(
            model_name='adress',
            name='DHCP',
            field=models.CharField(default='Sim', max_length=3),
        ),
        migrations.AddField(
            model_name='adress',
            name='DNS',
            field=models.CharField(default=2, max_length=255),
            preserve_default=False,
        ),
    ]
