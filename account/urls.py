from django.conf.urls import url
from .views import nav_login, registration, profile, logout

urlpatterns = [
    url(r'login/', nav_login, name='login'),
    url(r'registration/', registration, name='registration'),
    url(r'profile/', profile, name='profile'),
    url(r'logout/', logout, name='logout'),

]
