# Generated by Django 2.2.3 on 2019-09-29 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homesapp', '0004_auto_20190929_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='agent',
            name='member_since',
            field=models.DateField(null=True),
        ),
    ]
