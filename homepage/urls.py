from django.urls import path

from homepage.views import *

urlpatterns = [
    path('', home_page, name='home_page'),
    path('search/', search, name='search'),
]
