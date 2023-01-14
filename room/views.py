from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect

from .models import Room, Message

@login_required
def rooms(request):
    rooms = Room.objects.all()

    return render(request, 'room/ListeSalons.html', {'rooms': rooms})

@login_required
def room(request, slug):
    room = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room)[0:25]

    return render(request, 'room/Salon.html', {'room': room, 'messages': messages})


def add_room(request):
    if request.method == 'POST':
        form = request.POST
        name = form['name']
        slug = form['slug']
        room = Room(name=name, slug=slug)
        room.save()
        return redirect('rooms')
    else:
        return render(request, 'room/add_room.html')


