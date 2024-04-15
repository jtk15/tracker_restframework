# Generated by Django 4.2 on 2024-04-15 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='state_fk',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='core.state'),
        ),
    ]