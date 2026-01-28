from django.urls import path
from .views import *

app_name = 'main'

urlpatterns = [
    path('', get_home_page)
]