from inspect import stack
from django.contrib import admin
from django.urls import path
from .views.home import Index, store
from .views.signup import Signup
from .views.login import Login, logout
from .views.cart import Cart, delete_cart, DecreaseCart, IncreaseCart
from .views.mtr import Mt
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware


app_name = 'store'
urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('store', store , name='store'),
    path('material/', Mt.as_view() , name='materials'),
    path('signup/', Signup.as_view(), name='signup'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', logout , name='logout'),
    path('cart/', auth_middleware(Cart.as_view()), name='cart'),
    path('clean_cart/', auth_middleware(delete_cart), name='clean_cart'),
    path('increase_item_cart/<int:pk>/', auth_middleware(IncreaseCart.as_view()), name='increase_item_cart'),
    path('decrease_item_cart/<int:pk>/', auth_middleware(DecreaseCart.as_view()), name='decrease_item_cart'),
    path('check-out/', CheckOut.as_view() , name='checkout'),
    path('orders/', auth_middleware(OrderView.as_view()), name='orders'),
]
