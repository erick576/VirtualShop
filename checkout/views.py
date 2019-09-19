

# Gives response so that you can output anything onto the website

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index2.html')


