# Generated by Django 3.1.4 on 2021-02-05 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Products', '0009_auto_20210205_1644'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='condition',
            field=models.BooleanField(default=True, verbose_name='condition'),
        ),
    ]
