from django.shortcuts import render,redirect,get_object_or_404
from shop.models import*
from.models import *
from django.core.exceptions import ObjectDoesNotExist


# def cart_details(request,tot=0,count=0,cart_items=None):
#     try:
#         ct=cartlist.objects.get(cart_id=cart_id(request))
#         ct_items=items.objects.filter(cart=ct,active=true)
#         for i in ct_items:
#             tot+=(i.prodt.price*i.quan)
#             count+=i.quan
#     except ObjectDoesNotExist:
#          pass
#     return render(request,'cart.html',{'ci':ct_items,'t':tot,'cn':count})
def cart_details(request, tot=0, count=0, cart_items=None):
    ct_items = items.objects.none()  # Initialize ct_items to an empty queryset

    try:
        ct = cartlist.objects.get(cart_id=cart_id(request))
        ct_items = items.objects.filter(cart=ct, active=True)
        
        
        
        for i in ct_items:
            tot += (i.product.price * i.quantity)
            count += i.quantity
    except ObjectDoesNotExist:
        pass

    return render(request, 'cart.html', {'ci': ct_items, 't': tot, 'cn': count})


def cart_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id
def add_cart(request, product_id):
    prod = Products.objects.get(id=product_id)
    
    try:
        ct=cartlist.objects.get(cart_id=cart_id(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=cart_id(request))
        ct.save()

    try:
        c_items=items.objects.get(product=prod,cart=ct)
        if c_items.quantity < c_items.product.stock:
            c_items.quantity+=1
        c_items.save()
    except items.DoesNotExist:
        c_items=items.objects.create(product=prod,quantity=1,cart=ct)
        c_items.save()
    return redirect('cartDetails')

        
def min_cart(request, product_id):
    ct = cartlist.objects.get(cart_id=cart_id(request))
    prod = get_object_or_404(Products, id=product_id)
    c_items = items.objects.get(product=prod, cart=ct)
    if c_items.quantity > 1:
        c_items.quantity -= 1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartDetails')

def cart_delete(request, product_id):
    ct = cartlist.objects.get(cart_id=cart_id(request))
    prod = get_object_or_404(Products, id=product_id)
    c_items = items.objects.get(product=prod, cart=ct)
    c_items.delete()
    return redirect('cartDetails')


# def min_cart(request,product_id):
#     ct=cartlist.objects.get(cart_id=c_id(request))
#     prod=get_object_or_404(products,id=product_id)
#     c_items=cartlist.objects.get(product=prod,cart=ct)
#     if c_items.quantity>1:
#         c_items.quantity-=1
#         c_items.save()
#     else:
#         c_items.delete()
#     return redirect('cartDetails')

        
# def cart_delete(request,):
#     ct=cartlist.objects.get(cart_id=c_id(request))
#     prod=get_object_or_404(products,id=product_id)
#     c_items=cartlist.objects.get(product=prod,cart=ct)
#     return redirect('cartDetails')