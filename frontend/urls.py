from django.urls import path
from frontend.views import *

urlpatterns = [
    path('', index, name='index'),
    path('test/', test, name='test'),
]