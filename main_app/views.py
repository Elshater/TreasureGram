from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

name = 'Gold'
value = '1000'
context = {'treausre_name': name,
           'treausre_value': value}


def index(request):
    return render(request, 'index.html', context)
