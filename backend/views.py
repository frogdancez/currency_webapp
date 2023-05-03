from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse({"msg": "Hello Currency Webapp's Backend!"})
