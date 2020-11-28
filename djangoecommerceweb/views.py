from djangoecommerceweb.models import Product
from django.shortcuts import redirect, render
from django.urls import reverse
from djangoecommerceweb.forms import CustomUserCreationForm
from django.contrib.auth import login

def ecommerce_index(request):
    products = Product.objects.all()
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

def dashboard(request):
    return render(request, "users/dashboard.html")

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

def cart(request):
    return render(request, "cart.html")

def checkout(request):
    return render(request, "checkout.html")

def charge(request):
    return render(request, "charge.html")