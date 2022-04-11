from django.shortcuts import render
from .models import Product, Outlet


def home(request):
    shirts = Product.objects.filter(category='S')
    pants = Product.objects.filter(category='P')
    watches = Product.objects.filter(category='W')
    ties = Product.objects.filter(category='T')
    shoes = Product.objects.filter(category='SH')

    context = {
        'shirts': shirts,
        'pants': pants,
        'watches': watches,
        'ties': ties,
        'shoes': shoes,
    }
    return render(request, 'admin_panel/home.html', context)


def product_details(request, pk):
    product = Product.objects.get(id=pk)
    context = {
        'product': product,
    }
    return render(request, 'admin_panel/productdetail.html', context)


def shirts(request, data=None):
    if data is None:
        shirt = Product.objects.filter(category='S')
    elif data == 'below':
        shirt = Product.objects.filter(category='S').filter(discount_price__lt=1000)

    context = {
        'shirt': shirt,
    }
    return render(request, 'admin_panel/shirts.html', context)


def pants(request, data=None):
    if data is None:
        pant = Product.objects.filter(category='P')
    elif data == 'below':
        pant = Product.objects.filter(category='P').filter(discount_price__lt=1500)

    context = {
        'pant': pant,
    }
    return render(request, 'admin_panel/pants.html', context)


def watches(request, data=None):
    if data is None:
        watch = Product.objects.filter(category='W')
    elif data == 'below':
        watch = Product.objects.filter(category='W').filter(discount_price__lt=20000)

    context = {
        'watch': watch,
    }
    return render(request, 'admin_panel/watch.html', context)


def ties(request, data=None):
    if data is None:
        tie = Product.objects.filter(category='T')
    elif data == 'below':
        tie = Product.objects.filter(category='T').filter(discount_price__lt=800)

    context = {
        'tie': tie,
    }
    return render(request, 'admin_panel/tie.html', context)


def shoes(request, data=None):
    if data is None:
        shoe = Product.objects.filter(category='SH')
    elif data == 'below':
        shoe = Product.objects.filter(category='SH').filter(discount_price__lt=18000)

    context = {
        'shoe': shoe,
    }
    return render(request, 'admin_panel/shoes.html', context)
