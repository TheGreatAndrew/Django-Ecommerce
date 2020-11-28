from django.urls import path
from . import views
from django.conf.urls import include, url
from djangoecommerceweb.views import dashboard, register, checkout, charge

urlpatterns = [
    path("", views.ecommerce_index, name="ecommerce_index"),
    path("<int:pk>/", views.ecommerce_detail, name="ecommerce_detail"),
    # path(r"^dashboard", views.dashboard, name="dashboard"),
    path("cart", views.cart, name="cart"),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^register/", register, name="register"),
    url(r"^charge/", charge, name="charge"),
    url(r"^checkout/", checkout, name="checkout"),
    
]