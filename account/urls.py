from django.conf.urls import url
from .views import login, registration

urlpatterns = [
    url(r'login/', login, name='login'),
url(r'registration/', registration, name='registration'),
]
