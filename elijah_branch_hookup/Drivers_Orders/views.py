from django.shortcuts import render
from Drivers_Orders.models import Driver, Order
# Create your views here.

def Drivers_Orders_index(request):
    drivers = Driver.objects.all()
    orders = Order.objects.all()

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


