# Generated by Django 3.0.7 on 2020-06-08 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_phone_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='price',
            field=models.PositiveIntegerField(default=100000),
            preserve_default=False,
        ),
    ]
