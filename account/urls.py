from django.conf.urls import url
from .views import nav_login, registration, profile, logout, edit_profile, change_password

urlpatterns = [
    url(r'^login/$', nav_login, name='login'),
    url(r'^registration/$', registration, name='registration'),
    url(r'^profile/$', profile, name='profile'),
    url(r'^logout/$', logout, name='logout'),
    url(r'^profile/edit/$', edit_profile, name='edit_profile'),
    url(r'^profile/change-password/$', change_password, name='change_password'),
]
