# Generated by Django 3.0 on 2020-06-29 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_auto_20200629_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='ipadress',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='url',
            field=models.TextField(null=True),
        ),
    ]
