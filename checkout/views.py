import stripe as stripe
import os

from django.contrib import messages
from .models import OrderLineItem
from products.models import Product
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

# Set your secret key. Remember to switch to your live secret key in production!
# See your keys here: https://dashboard.stripe.com/account/apikeys
stripe.api_key = os.environ.get('STRIPE_SECRET_KEY')


# Token is created using Stripe Checkout or Elements!
# Get the payment token ID submitted by the form:


# Create your views here.
@login_required()
def checkout(request):

    if request.method == "POST":
        token = request.POST['stripeToken']

        cart = request.session.get('cart', {})
        total = 0

        for id, quantity in cart.items():
            product = get_object_or_404(Product, pk=id)
            total += quantity * product.price
            order_line_item = OrderLineItem(
                product=product,
                quantity=quantity
            )
            order_line_item.save()

        try:
            customer = stripe.Charge.create(
                amount=int(total * 100),
                currency="EUR",
                description=request.user.email,
                source=token
            )
            request.session['cart'] = {}
        except stripe.error.CardError:
            messages.error(request, "Your card was declined!")

        return render(request, "checkout.html")
    return render(request, "checkout.html")
