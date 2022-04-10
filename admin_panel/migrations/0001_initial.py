# Generated by Django 4.0.3 on 2022-04-10 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('selling_price', models.FloatField()),
                ('discount_price', models.FloatField()),
                ('descriptions', models.CharField(max_length=200)),
                ('brand', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('S', 'Shirts'), ('P', 'Pants'), ('W', 'Watch'), ('T', 'Tie'), ('SH', 'Shoes')], max_length=10)),
                ('product_image', models.ImageField(upload_to='product_image')),
            ],
        ),
    ]