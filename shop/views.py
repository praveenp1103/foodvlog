from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from .models import *  
from django.db.models import Q


def home(request, c_slug=None):
    c_page = None
    products_list = None

    if c_slug != None:
        c_page = get_object_or_404(Catog, slug=c_slug)
        products_list = Products.objects.filter(category=c_page)
        print("this is the product list")
        print(products_list)
    else:
        products_list = Products.objects.all() 
        print("this is the product list")
        print(products_list)
        paginator = Paginator(products_list, 3)
        try:
            page = int(request.GET.get('page', '1'))
        except:
            page = 1
        try:
            products = paginator.page(page)
            print("condition on this page")
        except (EmptyPage, InvalidPage):
            print("getting empty")
            products = paginator.page(paginator.num_pages)
        ct = Catog.objects.all()
    return render(request, "index.html", {'category': ct, 'products': products})

def ProdDetails(request, c_slug, Product_slug):
    print("inside the product details")
    try:
        prod = Products.objects.get(category__slug=c_slug, slug=Product_slug)
    except Exception as e:
        raise e
    return render(request, 'item.html', {'pr': prod})

def searching(request):
    prod = None
    query = None
    if 'q' in request.GET:
        query = request.GET.get('q')
        prod = Products.objects.all().filter(Q(name__contains=query) | Q(desc__contains=query))
    return render(request, 'search.html', {'qr': query, 'pr': prod})
