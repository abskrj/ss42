# Generated by Django 3.0 on 2020-05-09 19:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fake',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]