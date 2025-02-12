# Generated by Django 2.2.3 on 2019-09-29 00:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homesapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='favorite',
            field=models.ManyToManyField(blank=True, related_name='user_favourite', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='property',
            name='property_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homesapp.PropertyType'),
        ),
        migrations.AddField(
            model_name='property',
            name='user_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='agent',
            name='agency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='homesapp.RealEstateAgency'),
        ),
        migrations.AddField(
            model_name='agent',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
