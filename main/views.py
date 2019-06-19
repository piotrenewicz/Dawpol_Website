from django.shortcuts import render
# from django.template import loader
from .models import TextContent, ImageListing, ImageElement, ImageContent, Page

# Create your views here.


def index(request):
    logo = get_content_image("logo_1")
    page_list = Page.objects.all().order_by('order')
    context = {
        "logo": logo,
        "pages": page_list
    }
    # template = loader.render_to_string('main/index.html', context)
    # print(template)
    return render(request, 'main/index.html', context)


def parts_gallery(request):
    items = get_items("Baza_AutoCzęści")
    context = {
        "Parts": items
    }
    return render(request, 'main/parts.html', context)


def bus_rental(request):
    logo = get_content_image("logo_1")
    items = get_items("wynajem_busa")
    page_list = Page.objects.all().order_by('order')

    context = {
        "logo": logo,
        "photos": items,
        "pages": page_list,
    }
    return render(request, 'main/buspage.html', context)


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
