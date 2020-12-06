from django.contrib import admin
from djangoecommerceweb.models import Product
from djangoecommerceweb.models import Eli_Order

class ProductAdmin(admin.ModelAdmin):
    pass


class Eli_OrderAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
admin.site.register(Eli_Order, Eli_OrderAdmin)
