from django.urls import path
from . import views
from django.conf.urls import include, url
from djangoecommerceweb.views import dashboard, register, checkout, charge, Coupons_Ads_index, Drivers_Orders_index, Drivers_Orders_detail

urlpatterns = [
    path("", views.ecommerce_index, name="ecommerce_index"),
    path("<int:pk>/", views.ecommerce_detail, name="ecommerce_detail"),
    path("", views.Coupons_Ads_index, name="Coupons_Ads_index"),
    path("", views.Drivers_Orders_index, name="Drivers_Orders_index"),
    path("driver<int:pk>/", views.Drivers_Orders_detail, name="Drivers_Orders_detail"),

    # url(r"^\?q=\<int:pk\>/", views.ecommerce_detail, name="ecommerce_detail"),
    # url(r"^aaa\<int:pk\>", views.ecommerce_detail, name="ecommerce_detail"),

    path("cart<int:pk>", views.cart, name="cart"),
    # path(r"^dashboard", views.dashboard, name="dashboard"),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^register/", register, name="register"),
    url(r"^charge/", charge, name="charge"),
    url(r"^checkout/", checkout, name="checkout"),
    url(r"^coupons_ads/", Coupons_Ads_index, name="coupons_ads"),
    url(r"^drivers_orders/", Drivers_Orders_index, name="drivers_orders")
    
]