# Generated by Django 3.1.4 on 2021-01-07 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='address',
            options={'verbose_name': 'Address', 'verbose_name_plural': 'Addresses'},
        ),
        migrations.AlterModelOptions(
            name='shop',
            options={'verbose_name': 'Shop', 'verbose_name_plural': 'Shopes'},
        ),
        migrations.AlterModelOptions(
            name='useremail',
            options={'verbose_name': 'email', 'verbose_name_plural': 'emails'},
        ),
    ]
