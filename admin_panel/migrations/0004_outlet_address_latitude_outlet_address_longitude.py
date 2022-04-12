# Generated by Django 4.0.3 on 2022-04-12 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0003_remove_outlet_outlet_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='outlet',
            name='address_latitude',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='outlet',
            name='address_longitude',
            field=models.FloatField(default=0.0),
        ),
    ]
