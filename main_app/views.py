from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

name = 'Gold'
value = '1000'
context = {'treausre_name': name,
           'treausre_value': value}


def index(request):
    return render(request, 'index.html', {'treasures': treasures})


class Treasure:
    def __init__(self, name, value, material, location):
        self.name = name
        self.value = value
        self.material = material
        self.location = location


treasures = [
    Treasure("Gold", 5000, 'gold', 'gold'),
    Treasure("cofee", 1000, 'cofee', 'cofee'),
    Treasure("tea", 200, 'tea', 'tea'),
    Treasure("milk", 400, 'milk', 'milk'),
    Treasure("cheoklate", 0, 'cheoklate', 'cheoklate'),


]
