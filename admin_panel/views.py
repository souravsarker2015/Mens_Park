from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render

from .forms import RegistrationForm, OutletForm
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


def search_items(request):
    if request.method == 'GET':
        q = request.GET.get('q')
        multiple_q = Q(Q(title__icontains=q) | Q(brand__icontains=q))
        product = Product.objects.filter(multiple_q)

        if len(product) == 0:
            product = Product.objects.all()
        context = {
            'products': product
        }
        return render(request, 'admin_panel/search_item.html', context)


def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Registration has been done successfully!!!')
            form.save()
    else:
        form = RegistrationForm()
    context = {
        'form': form
    }
    return render(request, 'admin_panel/registration.html', context)


def outlet_add(request):
    if request.method == "POST":
        form = OutletForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            phone = form.cleaned_data['phone']
            manager_name = form.cleaned_data['manager_name']
            reg = Outlet(name=name, address=address, phone=phone, manager_name=manager_name)
            reg.save()
            messages.success(request, 'Outlet has been added !!')
        return render(request, 'admin_panel/dashboard.html', {'form': form, 'active': 'btn-primary'})
    else:
        form = OutletForm()
        return render(request, 'admin_panel/dashboard.html', {'form': form, 'active': 'btn-primary'})


def outlet_info(request):
    outlets = Outlet.objects.all()
    count_outlets = len(outlets)
    context = {
        'outlets': outlets,
        'count_outlets': count_outlets,
        'active': 'btn-primary',
    }
    return render(request, 'admin_panel/outlets_info.html', context)
