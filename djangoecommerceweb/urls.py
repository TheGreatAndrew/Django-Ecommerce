from django.urls import path
from . import views
from django.conf.urls import include, url
from djangoecommerceweb.views import dashboard, register, checkout, charge

urlpatterns = [
    path("", views.ecommerce_index, name="ecommerce_index"),
    path("<int:pk>/", views.ecommerce_detail, name="ecommerce_detail"),

    # url(r"^\?q=\<int:pk\>/", views.ecommerce_detail, name="ecommerce_detail"),
    # url(r"^aaa\<int:pk\>", views.ecommerce_detail, name="ecommerce_detail"),

    path("cart<int:pk>", views.cart, name="cart"),
    # path(r"^dashboard", views.dashboard, name="dashboard"),
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^register/", register, name="register"),
    url(r"^charge/", charge, name="charge"),
    url(r"^checkout/", checkout, name="checkout"),
    
]