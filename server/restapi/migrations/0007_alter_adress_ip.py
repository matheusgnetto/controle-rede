# Generated by Django 3.2.7 on 2021-10-23 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0006_auto_20211016_1515'),
    ]

    operations = [
        migrations.AlterField(
            model_name='adress',
            name='IP',
            field=models.GenericIPAddressField(),
        ),
    ]
