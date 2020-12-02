from django.db import models

# ~ Others
class Cart(models.Model):
    cart_id = models.IntegerField()

class Order(models.Model): 
    order_id = models.IntegerField()

class Coupon(models.Model):
    coupon_id = models.IntegerField()

# class DeliveryStatus(models.Model) : 
#     order_id = models.ForeignKey(Order)

class ShoppingHistory(models.Model) :
    shopping_id = models.IntegerField()

# ~ Product 
class ProductCategory(models.Model):
    category_name = models.CharField(max_length=20)

class Product(models.Model):
    product_name = models.CharField(max_length=20)
    product_description = models.TextField()
    product_imageUrl = models.TextField()
    product_price = models.IntegerField()
    # product_image = models.FilePathField(path="/img")

# ~ Users
class Shopper(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=20)
    user_image = models.FilePathField(path="/img")
    credit_card = models.IntegerField()
    # shoppinghistory models.ForeignKey(ShoppingHistory)

class Manager(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=20)
    user_image = models.FilePathField(path="/img")

class StorageMaintainer(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=20)
    user_image = models.FilePathField(path="/img")

class DeliveryDriver(models.Model):
    user_id = models.IntegerField()
    username = models.CharField(max_length=20)    
    user_image = models.FilePathField(path="/img")

# Elijah Models
class Eli_Coupon(models.Model):
    product_name = models.CharField(max_length=100)
    product_price = models.DecimalField(max_digits=5, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.FilePathField(path="/img")


class Ad(models.Model):
    image = models.FilePathField(path="/img")
    product_name = models.CharField(max_length=100)

class Driver(models.Model):
    name = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=12)
    availability = models.CharField(max_length=15) 
    location = models.CharField(max_length=200)
    is_available = models.BooleanField(default=True)
    order = models.CharField(max_length=150, default="Not Assigned")
    image = models.FilePathField(path="/img")


class Eli_Order(models.Model):
    store = models.CharField(max_length=60)
    customer_name = models.CharField(max_length=70)
    item_count = models.IntegerField(default=0)
    image = models.FilePathField(path="/img")

