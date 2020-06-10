from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Feed


# Create your views here.
@login_required()
def view_feed(request):
    feed_elements = Feed.objects.all()
    if request.user.is_authenticated:
        return render(request, "feed.html", {"feed_elements": feed_elements})
    else:
        return render(request, "index.html")
