"""LastMilestoneProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from home import urls as home_urls
from account import urls as account_urls
from feed import urls as feed_urls
from products import urls as urls_product
from cart import urls as urls_cart
from search import urls as search_urls
from checkout import urls as urls_checkout

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^', include(home_urls), name='index'),
    url('account/', include(account_urls)),
    url(r'^feed/', include(feed_urls)),
    url(r'^products/', include(urls_product)),
    url(r'^cart/', include(urls_cart)),
    url(r'^search/', include(search_urls)),
    url(r'^checkout/', include(urls_checkout)),
]
