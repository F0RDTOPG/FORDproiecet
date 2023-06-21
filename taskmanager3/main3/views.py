from django.shortcuts import render
from . models import Room


rooms = [
    {'id':1,'name':'MySQL'},
    {'id':2,'name':'SQL Server'},
    {'id':3,'name':'MongoDB'},
]


def home(request):
        rooms = Room.objects.all()
        context = {'rooms': rooms}
        return render(request, 'main3/home.html', context)

def room(request,pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'main3/room.html', context)
# Create your views here.
