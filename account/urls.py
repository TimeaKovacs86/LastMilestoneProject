from django.conf.urls import url
from .views import nav_login, nav_registration, nav_profile, logout

urlpatterns = [
    url(r'login/', nav_login, name='login'),
    url(r'registration/', nav_registration, name='registration'),
    url(r'profile/', nav_profile, name='profile'),
    url(r'logout/', logout, name='logout'),

]
