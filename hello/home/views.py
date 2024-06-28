from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
def index(request):
    return render(request, 'index.html')

def seemore(request):
    return render(request, 'seemore.html')

def seemore(request):
    # Fetch all CartItem objects from the database
    cart_items = CartItem.objects.all()

    # Calculate total price
    total_price = sum(item.price for item in cart_items)

    context = {
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'seemore.html', context)

def delete_item(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id)
    item.delete()
    return redirect('seemore')
                  

from django.shortcuts import render, redirect
from .models import CartItem
from .forms import AddToCartForm

# cart/views.py

from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import CartItem

@require_POST
def add_to_cart(request):
    product_name = request.POST.get('product_name')
    price = request.POST.get('price')

    # Create a CartItem instance
    cart_item = CartItem(name=product_name, price=price)
    cart_item.save()

    return redirect('seemore')  # Replace 'seemore' with your actual redirect URL
