from django.shortcuts import render, redirect, reverse
from django.contrib import messages


# Create your views here.
def view_cart(request):
    return render(request, "cart.html")


def add_to_cart(request, id):
    if request.POST.get('quantity') == "":
        messages.info(request, "The input field is empty!")
        return redirect(reverse('products'))
    else:
        quantity = int(request.POST.get('quantity'))

    cart = request.session.get('cart', {})
    if id in cart:
        messages.info(request, "Item has given to the cart!")
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)
        messages.info(request, "Item has given to the cart!")
    request.session['cart'] = cart
    return redirect(reverse('products'))


def adjust_cart(request, id):
    if request.POST.get('quantity') == "":
        messages.add_message(request, messages.INFO, "We can't modify empty input!")
        return redirect(reverse('view_cart'))
    else:
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})

    if quantity > 0:
        messages.info(request, "You modified the number of the items!")
        cart[id] = quantity
    else:
        return redirect(reverse('view_cart'))

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


def delete_cart(request, id):
    cart = request.session.get('cart', {})
    cart.pop(id)
    request.session['cart'] = cart
    messages.info(request, "Item has been deleted!")
    return redirect(reverse('view_cart'))
