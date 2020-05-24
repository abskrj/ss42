# Generated by Django 2.2.12 on 2020-05-24 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Developers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dev_name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('ssEmail', models.EmailField(max_length=254)),
                ('company', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=255)),
                ('description', models.TextField(max_length=1024)),
                ('token', models.TextField(max_length=1024, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
