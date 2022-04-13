from django.db import models
from django.utils import timezone

CATEGORY_CHOICES = (
    ('S', 'Shirts'),
    ('P', 'Pants'),
    ('W', 'Watch'),
    ('T', 'Tie'),
    ('SH', 'Shoes'),
)


class Product(models.Model):
    title = models.CharField(max_length=50)
    selling_price = models.FloatField()
    discount_price = models.FloatField()
    descriptions = models.CharField(max_length=200)
    brand = models.CharField(max_length=100)
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    product_image = models.ImageField(upload_to='product_image')

    def __str__(self):
        return str(self.id)


class Outlet(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.IntegerField()
    manager_name = models.CharField(max_length=50)
    address_latitude = models.FloatField(default=0.0, blank=True, null=True)
    address_longitude = models.FloatField(default=0.0, blank=True, null=True)
    opening_time = models.TimeField(default=timezone.now, blank=True, null=True)
    closing_time = models.TimeField(default=timezone.now, blank=True, null=True)
    off_day = models.CharField(default="Friday", max_length=50, blank=True, null=True)
    outlet_image = models.ImageField(upload_to='outlet_image', default='outlet_image/menspark_default_hrIJzS0.jpg', blank=True, null=True)

    def __str__(self):
        return self.name
