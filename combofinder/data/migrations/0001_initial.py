# Generated by Django 4.0.6 on 2022-07-16 18:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='userData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upper_limit', models.IntegerField()),
                ('lower_limit', models.IntegerField()),
                ('doc', models.FileField(upload_to='', validators=[django.core.validators.FileExtensionValidator(['csv'])])),
                ('email', models.EmailField(default=None, max_length=254)),
            ],
        ),
    ]
