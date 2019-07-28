from django.shortcuts import render

# Create your views here.

def info(request):
    return render(request, 'contact/info.html')

def map(request):
    return render(request, 'contact/map.html')

def full_map(request):
    return render(request, "contact/fullmap.html")