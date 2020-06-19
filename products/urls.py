from django.conf.urls import url
from .views import all_products, view_product

urlpatterns = [
    url(r'^$', all_products, name='products'),
    url(r'^(?P<slug>[\w-]+)/$', view_product, name='view_product_detail')
]
