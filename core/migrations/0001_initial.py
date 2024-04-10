# Generated by Django 4.2 on 2024-04-10 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Estado')),
                ('abbreviation', models.CharField(max_length=2, verbose_name='Sigla')),
            ],
        ),
    ]