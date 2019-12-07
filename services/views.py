from django.shortcuts import render

# Create your views here.


def wip(request):
    return render(request, 'services/wip.html')


def service(request):
    return render(request, 'services/our_services.html')