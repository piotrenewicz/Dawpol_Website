from django.shortcuts import render

# Create your views here.

def map(request):
    return render(request, 'contact/map.html')

def full_map(request):
    return render(request, "contact/fullmap.html")