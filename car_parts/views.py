from django.shortcuts import render

# Create your views here.


def part(request):
    return render(request, 'car_parts/our_parts.html')
