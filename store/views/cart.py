from django.shortcuts import render , redirect

from django.contrib.auth.hashers import  check_password
from store.models.customer import Customer
from django.views import  View
from store.models.product import Products

class Cart(View):
    def get(self , request):
        ids = list(request.session.get('cart').keys())
        # print(request.session.get('cart'))
        products = Products.get_products_by_id(ids)
        print(ids, products)
        return render(request , 'cart.html' , {'products' : products})


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


