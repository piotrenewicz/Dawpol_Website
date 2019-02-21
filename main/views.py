from django.shortcuts import render
from django.template import loader
from .models import Content

# Create your views here.

def index(request):
    context = {

    }
    # template = loader.render_to_string('main/index.html', context)
    # print(template)
    return render(request, 'main/index.html', context)


def com_list(request):
    contents = Content.objects.all()
    context = {
        "comments": contents
    }
    return render(request, 'main/happy.html', context)
