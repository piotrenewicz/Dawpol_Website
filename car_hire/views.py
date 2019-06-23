from django.shortcuts import render
from main.views import get_items

# Create your views here.


def overview(request):
    items = get_items("wynajem_busa")
    context = {
        "photos": items,
    }
    return render(request, 'car_hire/buspage.html', context)


def detailedview(request, car_id):
    return render(request, 'car_hire/buspage.html', car_id) # TODO: don't call this yet, it's unfinished
