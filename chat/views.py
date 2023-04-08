from django.shortcuts import render
from django.contrib import messages

def index(request):
    return render(request, 'index.html', {})

def room(request, room_name):
    return render(request, 'chatroom.html', {"room_name": room_name})