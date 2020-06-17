from django.shortcuts import render
from products.models import Product


# Create your views here.
def search(request):
    products = Product.objects.filter(name__contains=request.GET['search'])
    is_empty = bool(products)
    return render(request, "products.html", {"products": products, "is_empty": is_empty})
