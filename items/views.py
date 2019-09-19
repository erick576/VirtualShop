from django.http import HttpResponse  # Gives response so that you can output anything onto the website
from django.shortcuts import render
from . models import Item


# /items -> index  // URLS
def index(request):
    items = Item.objects.all()
    return render(request, 'index.html', {'items': items})


def new(request):
    return HttpResponse('New Products')