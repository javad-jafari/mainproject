# Generated by Django 3.1.4 on 2021-02-06 15:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0011_auto_20210206_1903'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='create_at',
        ),
        migrations.RemoveField(
            model_name='like',
            name='update_at',
        ),
    ]
