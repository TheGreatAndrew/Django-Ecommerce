from django.shortcuts import redirect, render
from django.urls import reverse
from djangoecommerceweb.forms import CustomUserCreationForm
from django.contrib.auth import login
from djangoecommerceweb.models import Eli_Coupon, Ad
from djangoecommerceweb.models import Eli_Order, Driver
from djangoecommerceweb.models import Product

from djangoecommerceweb.forms import DriverForm

def ecommerce_index(request):
    products = Product.objects.all()
    print("hello andrew")
    context = {
        'products': products
    }
    return render(request, 'ecommerce_index.html', context)

def ecommerce_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, 'ecommerce_detail.html', context)


def cart(request, pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product': product
    }
    return render(request, "cart.html", context)

def dashboard(request):
    return render(request, "users/dashboard.html")

def shopper_dashboard(request):
    return render(request, "users/shopper_dashboard.html")

def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("dashboard"))

def checkout(request):
    return render(request, "checkout.html")

def charge(request):
    return render(request, "charge.html")

def Coupons_Ads_index(request):
    coupons = Eli_Coupon.objects.all()
    ads = Ad.objects.all()

    context = {
            'coupons': coupons,
            'ads': ads
    }

    return render(request, 'Coupons_Ads_index.html', context)   


def Drivers_Orders_index(request):
    drivers = Driver.objects.all()
    orders = Eli_Order.objects.all()

    context = {
                'drivers': drivers,
                'orders': orders
    }
    
    return render(request, 'Drivers_Orders_index.html', context)


def Drivers_Orders_detail(request, pk):
    drivers = Driver.objects.get(pk=pk)
    context = {
        'drivers': drivers

    }
    return render(request, 'Drivers_Orders_detail.html', context)

def Drivers_Orders_detail_assign(request, pk):
    drivers = Driver.objects.get(pk=pk)

    context = {
        'drivers': drivers

    }
    drivers.is_available = False;

    if drivers.name == "Rhea Nova":
        drivers.order = "Store: H-E-B\nCustomer: Karen Chandler\nItem Count: 145\n"

    elif drivers.name == "Cruz Garza":
        drivers.order = "Store: Whole Foods\nCustomer: David Rodriguez\nItem Count: 80\n"

    elif drivers.name == "Cory Terry-Cook":
        drivers.order = "Store: Petsmart\nCustomer: Ginger Casey\nItem Count: 57\n"



    return render(request, "Drivers_Orders_detail.html", context)