from django.shortcuts import render


# Create your views here.
def search(request):
    is_empty = request.GET['search']
    return render(request, "products.html", { "is_empty": is_empty})
