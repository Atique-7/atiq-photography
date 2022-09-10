from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Picture, Filter, User, Order
from .models.forms import RegistrationForm, LoginForm
from django.views import View


# Create your views here.

    
class Detail(View):
    def get(self, request, pagename):
        name = pagename
        productInfo = Picture.objects.get(permalink=name)
        context = {'ProductInfo' : productInfo}
        return render(request, 'store/product_detail.html', context)

    def post(self, request, pagename):
        #handling the "add to cart" request.
        order = request.POST.get('product')
        remove = request.POST.get('remove')
        cart = request.session.get('cart')

        #checking if the cart exists.
        if cart:
            cart[order] = 1
            if remove:
                cart.pop(order)
        else:
            cart = {}
            cart[order] = 1

        #Checking if the cart already exists.
        request.session['cart'] = cart

        #Getting back to the same Page.
        name = pagename
        productInfo = Picture.objects.get(permalink=name)
        context = {'ProductInfo' : productInfo}    
        return render(request, 'store/product_detail.html', context)


class Signup(View):
    def get(self, request):
        form = RegistrationForm()
        context = {'form': form}
        return render(request, 'modelsignup.html', context)

    def post(self, request):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('store')
        context = {'form': form}
        return render(request, 'modelsignup.html', context)


class Login(View):
    def get(self, request):
        error = False
        form = LoginForm()
        context = {'form': form, 'error': error}
        return render(request, 'login.html', context)

    def post(self, request):
        error = False
        form = LoginForm(data=request.POST)
        email = request.POST.get('email')
        if form.is_valid():

            #session Handling
            customer = User.get_customer(email)
            request.session['user_id'] = customer.id
            request.session['user_email'] = customer.email

            #redirection to homepage after successful login
            return redirect('store')

        else:
            error = True

        context = {'form': form, 'error': error}
        return render(request, 'login.html', context)
    

def logout(request):
    request.session.clear()
    return redirect('home')


def cart(request):
    ids = list(request.session.get('cart').keys())
    cart_items = Picture.getProductsbyId(ids)
    context = {'items': cart_items}
    return render(request, 'store/cart.html', context)


def home(request):
    return render(request, 'home.html')


def store(request):
    # cart = request.session.get('cart')
    # if not cart:
    #     request.session.cart = {}
    product_data = None
    category_data = Filter.get_all_categories()
    sort_id = request.GET.get('id')
    if sort_id:
        product_data = Picture.get_all_pieces_by_sort(sort_id)
    else:
        product_data = Picture.get_all_pieces()
        
    context = {'DataList' : product_data,
                'Categories' : category_data,
                }
    return render(request, 'store/store.html', context)


class Checkout(View):
    def post(self, request):
        customer = request.session.get('user_id')
        #Getting the products
        cart = request.session.get('cart')
        products = Picture.getProductsbyId(list(cart.keys()))
        for product in products:
            order = Order(
                product=product,
                customer = User(id = customer),
                price = product.price,
            )
            #saving every order as single object.
            order.placeOrder()
        request.session['cart'] = {}
        return redirect('store')


class OrderView(View):
    def get(self, request):
        customer = request.session.get('user_id')
        order = Order.getOrderByCustomer(customer)
        context = {'items': order}
        return render(request, 'store/orders.html', context)