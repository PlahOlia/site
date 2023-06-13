from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import Products
from store.models.orders import Order

class Cart(View):
    def get(self, request):
        print('9')
        ids = list(request.session.get('cart').keys())
        products = Products.get_products_by_id(ids)
        print(ids, products)
        return render(request , 'cart.html' , {'products' : products})
    
    def post(self, request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Products.get_products_by_id(list(cart.keys()))
        print(address, phone, customer, cart, products)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          price=product.price,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('store:cart')


def delete_cart(request):
    request.session['cart'] = {}
    return redirect('store:cart')


class IncreaseCart(View):
    def get(self, request):
        pk = request.META['PATH_INFO'].split('/')[2]
        request.session['cart'][pk] = request.session['cart'][pk] + 1
        return redirect('store:cart')

class DecreaseCart(View):
    def get(self, request):
        pk = request.META['PATH_INFO'].split('/')[2]
        if request.session['cart'][pk] > 1:
            request.session['cart'][pk] -= 1
        return redirect('store:cart')


