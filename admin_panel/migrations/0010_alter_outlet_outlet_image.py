# Generated by Django 4.0.3 on 2022-04-13 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0009_outlet_outlet_image_alter_outlet_off_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outlet',
            name='outlet_image',
            field=models.ImageField(blank=True, default='menspark_default.jpg', null=True, upload_to='outlet_image'),
        ),
    ]
