from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from .models import *

from .forms import *


def index(request):
    return render(request, 'inv/index.html')
   
def home(request):
    return render(request, 'inv/index.html')
   

def display_foods(request):
    items = Foods.objects.all()
    context = {
        'items': items,
        'header': 'Foods',
    }
    return render(request, 'inv/index.html', context)


def display_drinks(request):
    items = Drinks.objects.all()
    context = {
        'items': items,
        'header': 'Drinks',
    }
    return render(request, 'inv/index.html', context)


def display_others(request):
    items = Others.objects.all()
    context = {
        'items': items,
        'header': 'Others',
    }
    return render(request, 'inv/index.html', context)

def add_item(request, cls):
    if request.method == "POST":
        form = cls(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = cls()
        return render(request, 'inv/add_new.html', {'form' : form})


def add_food(request):
    return add_item(request, FoodForm)


def add_drink(request):
    return add_item(request, DrinkForm)


def add_other(request):
    return add_item(request, OtherForm)


def edit_item(request, pk, model, cls):
    item = get_object_or_404(model, pk=pk)

    if request.method == "POST":
        form = cls(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = cls(instance=item)

        return render(request, 'inv/edit_item.html', {'form': form})



def edit_food(request, pk):
    return edit_item(request, pk, Foods, FoodForm)


def edit_drink(request, pk):
    return edit_item(request, pk, Drinks, DrinkForm)


def edit_other(request, pk):
    return edit_item(request, pk, Others, OtherForm)


def delete_food(request, pk):

    template = 'inv/index.html'
    Foods.objects.filter(id=pk).delete()

    items = Foods.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_drink(request, pk):

    template = 'inv/index.html'
    Drinks.objects.filter(id=pk).delete()

    items = Drinks.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)


def delete_other(request, pk):

    template = 'inv/index.html'
    Others.objects.filter(id=pk).delete()

    items = Others.objects.all()

    context = {
        'items': items,
    }

    return render(request, template, context)
