# Generated by Django 3.0.7 on 2020-06-06 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200, unique=True)),
                ('userid', models.IntegerField()),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('delivery_address', models.CharField(max_length=200, unique=True)),
                ('phone_number', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
