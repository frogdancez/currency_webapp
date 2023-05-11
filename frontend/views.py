from django.shortcuts import render
from backend.data import interest_rates

def test(request):
    return render(request, 'test.html')

def home(request):
    context = {
        'currencies': list(interest_rates.keys())
    }
    return render(request, 'home.html', context=context)

def news(request):
    return render(request, 'news.html')

def trade(request):
    return render(request, 'trade.html')

def about_us(request):
    return render(request, 'about_us.html')

def info(request, currency):
    context = {
        'currency': currency
    }
    return render(request, 'info.html', context=context)
