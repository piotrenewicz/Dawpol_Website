from django.shortcuts import render

# Create your views here.


def service(request):
    return render(request, 'services/our_services.html')