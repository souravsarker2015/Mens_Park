# Generated by Django 4.0.3 on 2022-04-13 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0004_outlet_address_latitude_outlet_address_longitude'),
    ]

    operations = [
        migrations.CreateModel(
            name='OutletTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
            ],
        ),
    ]
