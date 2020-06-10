from django.conf.urls import url
from .views import view_feed

urlpatterns = [
    url(r'^$', view_feed, name='feed')
]