# Generated by Django 3.0.7 on 2020-06-08 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='phone',
            name='picture',
            field=models.ImageField(blank=True, upload_to='phone_pics'),
        ),
    ]