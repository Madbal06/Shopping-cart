from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Product, Order

def product_catalog(request):
    products = Product.objects.all()
    return render(request, 'product_catalog.html', {'products': products})

def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = Product.objects.get(id=product_id)
        quantity = int(request.POST['quantity'])
        Order.objects.create(user=request.user, product=product, quantity=quantity)
    return redirect('product_catalog')

def view_cart(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'cart.html', {'orders': orders})

def checkout(request):
    if request.method == 'POST':
        # Process the payment and shipping information
        # Generate an order confirmation and store it in the database
        # Redirect to order confirmation page
        return redirect('order_confirmation')
    return render(request, 'checkout.html')

def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_history.html', {'orders': orders})


