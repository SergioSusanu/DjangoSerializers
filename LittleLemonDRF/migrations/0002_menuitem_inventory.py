# Generated by Django 5.0.3 on 2024-03-23 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LittleLemonDRF', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='inventory',
            field=models.IntegerField(default=0),
        ),
    ]
