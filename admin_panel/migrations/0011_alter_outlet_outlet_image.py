# Generated by Django 4.0.3 on 2022-04-13 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0010_alter_outlet_outlet_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='outlet',
            name='outlet_image',
            field=models.ImageField(blank=True, default='outlet_image/menspark_default_hrIJzS0.jpg', null=True, upload_to='outlet_image'),
        ),
    ]
