from django.conf.urls import url
from .views import index
from home import views as home_views
from django.conf.urls import handler404

urlpatterns = [
    url(r'^$', index, name='index'),
]

handler404 = home_views.error_404
