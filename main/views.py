from django.shortcuts import render
# from django.template import loader
from .models import TextContent, ImageListing, ImageElement, ImageContent, Page

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def parts_gallery(request):
    items = get_items("Baza_AutoCzęści")
    context = {
        "Parts": items
    }
    return render(request, 'main/parts.html', context)


def get_content_image(image_name):
    image = ImageContent.objects.get(name=image_name)
    return image


def get_items(item_manager_name):
    items_manager = ImageListing.objects.get(id=item_manager_name)
    all_items = items_manager.imageelement_set.all()
    return all_items


def items_view(request, item_manager_name):
    items = get_items(item_manager_name)
    context = {
        "graphical_items": items
    }
    return render(request, 'main/generic_tiles.html', context)


def com_list(request):
    contents = TextContent.objects.all()
    context = {
        "comments": contents
    }
    return render(request, 'main/happy.html', context)
