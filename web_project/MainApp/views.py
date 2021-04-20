from django.shortcuts import render , redirect
from .models import Product , Category , Cart , CartItem 




def home(request) :
    
    products = Product.objects.all()
    categoies = Category.objects.all()
    
    return render(request, 'home.html',{'products' : products , 'categoies' : categoies})


def product_detail(request, product_slug):
    try :
        product_detail = Product.objects.get(slug=product_slug) 
    except Exception as e :
        raise e
    return render(request , 'product_detail.html' , {'product_detail' : product_detail })


# We create cart_id
def _cart_id(request) :
    cart = request.session.session_key
    if not cart : 
        cart = request.session.create()
    return cart


def add_cart(request, product_id) :
    product = Product.objects.get(id=product_id)
    try :
        cart = Cart.objects.get(cart_id=_cart_id(request))
    except Cart.DoesNotExist :
        cart = Cart.objects.create(cart_id=_cart_id(request))
        cart.save()
    try :
        cart_item = CartItem.objects.get(product=product)
        cart_item.quantity += 1
        cart_item.save()
        
    except CartItem.DoesNotExist :
        cart_item = CartItem.objects.create(
            product = product,
            quantity = 1 ,
            cart = cart ,
        )
        cart_item.save()
    
    return redirect('cart.html')

def cart(request) :
    return render(request, 'cart.html')
