# Generated by Django 4.0.3 on 2022-04-13 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0008_alter_outlet_address_latitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='outlet',
            name='outlet_image',
            field=models.ImageField(blank=True, default='menspark_default', null=True, upload_to='outlet_image'),
        ),
        migrations.AlterField(
            model_name='outlet',
            name='off_day',
            field=models.CharField(blank=True, default='Friday', max_length=50, null=True),
        ),
    ]
