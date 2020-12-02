from django.db import models

# Create your models here.

class Coupon(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.FilePathField(path="/img")


class Ad(models.Model):
    image = models.FilePathField(path="/img")
    product_name = models.CharField(max_length=100)