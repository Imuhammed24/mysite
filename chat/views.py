from django.shortcuts import render
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()


def index(request):
    user = User.objects.get(username='admin2')

    context = {
        'user': user
    }

    return render(request, 'chat/index.html', context)


def room(request, room_name):
    return render(request, 'chat/room.html', {'room_name': room_name})
