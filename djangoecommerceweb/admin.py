from django.contrib import admin
from djangoecommerceweb.models import Product

class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Product, ProductAdmin)
