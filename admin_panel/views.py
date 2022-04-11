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

    return render(request, 'admin_panel/home.html',context)


