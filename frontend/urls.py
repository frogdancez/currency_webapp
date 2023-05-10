from django.urls import path
from frontend.views import *

urlpatterns = [
    path('', home, name='home'),
    path('test/', test, name='test'),
    path('trade/', trade, name='trade'),
    path('about_us/', about_us, name='about_us'),
    path('news/', news, name='news'),

    path('info/<str:currency>', info, name='info'),
]