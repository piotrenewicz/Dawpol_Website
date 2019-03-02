from django.shortcuts import render
from django.template import loader
from .models import Content, GraphicalItemManager, GraphicalItem

# Create your views here.


def index(request):
    context = {

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


def get_items(item_manager_name):
    items_manager = GraphicalItemManager.objects.get(id=item_manager_name)
    all_items = items_manager.graphicalitem_set.all()
    return all_items


def items_view(request, item_manager_name):
    items = get_items(item_manager_name)
    context = {
        "graphical_items": items
    }
    return render(request, 'main/generic_tiles.html', context)


def com_list(request):
    contents = Content.objects.all()
    context = {
        "comments": contents
    }
    return render(request, 'main/happy.html', context)
