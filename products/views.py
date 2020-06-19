from django.shortcuts import render
from .models import Product, Review
from .forms import ReviewForm
from django.contrib import messages


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    is_empty = True
    return render(request, "products.html", {"products": products, "is_empty": is_empty})


def view_product(request, slug):
    product = Product.objects.get(slug=slug)
    reviews = Review.objects.filter(product=product)
    if request.method == "POST":
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            model_instance = review_form.save(commit=False)
            model_instance.product = product
            model_instance.author = request.user
            model_instance.save()
            messages.success(request, "Review added")
            return render(request, "view-product.html", {
                "product": product,
                "reviews": reviews,
                "review_form": ReviewForm()
            })
    else:
        review_form = ReviewForm()

    return render(request, "view-product.html", {
        "product": product,
        "reviews": reviews,
        "review_form": review_form
    })
