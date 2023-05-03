from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, 'test.html')

def home(request):
    return render(request, 'home.html')

def news(request):
    return render(request, 'news.html')

def trade(request):
    return render(request, 'trade.html')

def about_us(request):
    return render(request, 'about_us.html')
