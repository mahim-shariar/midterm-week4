# Generated by Django 5.0.6 on 2024-07-11 18:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0003_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='email',
        ),
    ]
