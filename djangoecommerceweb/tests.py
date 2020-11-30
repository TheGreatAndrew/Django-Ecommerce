from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from djangoecommerceweb.models import Product, Cart, Order

# Create your tests here.
class TestClass(TestCase) : 
    def test_basic(self):
        a = 1
        self.assertEqual(1, a)

    def test_product1(self) : 
        product = Product.objects.create(product_name="Testing", product_description="a", 
            product_imageUrl="a", product_price=1)
        self.assertEqual(product.product_name, "Testing")

    def test_product2(self) : 
        product = Product.objects.create(product_name="Testing", product_description="a", 
            product_imageUrl="a", product_price=1)
        self.assertIsInstance(product, Product)

    def test_cart(self):
        cart = Cart.objects.create(cart_id=99)
        self.assertIsInstance(cart, Cart)
    
    def test_order(self):
        order = Order.objects.create(order_id=99)
        self.assertIsInstance(order, Order)
    