from django.db import models

# Create your models here.

class Driver(models.Model):
    name = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=12)
    availability = models.CharField(max_length=15) 
    location = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    order = models.CharField(max_length=150, default="Not Assigned")
    image = models.FilePathField(path="/img")


class Order(models.Model):
    store = models.CharField(max_length=60)
    customer_name = models.CharField(max_length=70)
    item_count = models.IntegerField(default=0)
    image = models.FilePathField(path="/img")

