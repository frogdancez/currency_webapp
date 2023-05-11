from django.http import HttpResponse
from django.http import JsonResponse
from backend.data import interest_rates
import requests
from datetime import datetime, timedelta

# Create your views here.
def index(request):
    return JsonResponse({"msg": "Hello Currency Webapp's Backend!"})

def spot(request, currency1, currency2):
    try:
        url = 'https://api.exchangerate.host/latest?base=' + currency1
        response = requests.get(url)
        result = response.json()
        return JsonResponse({str(currency1) + '/' + str(currency2) : result['rates'][currency2]})
    except Exception as e:
        return JsonResponse({"error": e})
    
def forward(request, currency1, currency2):
    try:
        i_currency1 = interest_rates[currency1]
        i_currency2 = interest_rates[currency2]

        url = 'https://api.exchangerate.host/latest?base=' + currency1
        response = requests.get(url)
        result = response.json()

        return JsonResponse({"forward_rate " + str(currency1) + '/' + str(currency2) : result['rates'][currency2] * (1 + i_currency1) / (1 + i_currency2)})
    except Exception as e:
        return JsonResponse({"error": e})
    
def history(request, currency):
    try:
        end = datetime.now()
        start = end - timedelta(days=7) # get data from range a week

        url = 'https://api.exchangerate.host/timeseries?base=' + currency + "&start_date=" + str(start.strftime("%Y-%m-%d")) + "&end_date=" + str(end.strftime("%Y-%m-%d"))
        response = requests.get(url)
        result = response.json()

        return JsonResponse(result)
    except Exception as e:
        return JsonResponse({"error": e})