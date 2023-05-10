from django.urls import path
from backend.views import *

urlpatterns = [
    path('', index, name='index'),
    path('spot/<str:currency1>/<str:currency2>', spot, name='spot'),
    path('forward/<str:currency1>/<str:currency2>', forward, name='forward'),
]