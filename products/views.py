from django.shortcuts import render
from .models import Product


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    is_empty = True
    return render(request, "products.html", {"products": products, "is_empty": is_empty})
