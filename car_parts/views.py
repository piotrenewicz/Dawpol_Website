from django.shortcuts import render

# Create your views here.

def wip(request):
    return render(request, 'car_parts/wip.html')
