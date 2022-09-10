from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('store', views.store, name='store'),
    path('store/<str:pagename>', views.Detail.as_view(), name='detail'),
    path('signup', views.Signup.as_view(), name='signup'),
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.logout, name='logout'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.Checkout.as_view(), name='checkout'),
    path('orders', views.OrderView.as_view(), name='orders'),
]