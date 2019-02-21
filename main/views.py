from django.shortcuts import render
from django.template import loader
from .models import Comment

# Create your views here.

def index(request):
    context = {

    }
    # template = loader.render_to_string('main/index.html', context)
    # print(template)
    return render(request, 'main/index.html', context)


def com_list(request):
    comments = Comment.objects.all()
    context = {
        "comments": comments
    }
    return render(request, 'main/happy.html', context)
