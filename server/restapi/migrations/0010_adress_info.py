# Generated by Django 3.2.7 on 2021-11-02 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0009_auto_20211030_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='adress',
            name='info',
            field=models.TextField(blank=True, max_length=255, null=True),
        ),
    ]