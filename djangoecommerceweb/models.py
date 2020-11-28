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
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=20)
    product_description = models.TextField()
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
