from django.shortcuts import render
from car_hire.models import Car
from main.views import get_items

# Create your views here.


def overview(request):
    all_cars = Car.objects.all()
    for car in all_cars:
        car.short_description = car.description.split("\n")[0]
    context = {
        'cars': all_cars,
    }
    return render(request, 'car_hire/overview.html', context)


def detailedview(request, car_id):
    certain_car = Car.objects.get(id=car_id)
    context = {
        'car': certain_car,
    }

    return render(request, 'car_hire/detailed.html', context)
