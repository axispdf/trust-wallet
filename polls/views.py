from django.shortcuts import render
from polls.models import *
from polls.forms import *


User = settings.AUTH_USER_MODEL

def index(request): 
    user = User
    bio = Bio.objects.all()
    context = {
        'user': user,
        'bio': bio
    }
    return render(request, 'djangoMain/index.html', context)


def send(request):
    user = User
    bio = Bio.objects.all()
    context = {
        'user': user,
        'bio': bio
    }
    return render(request, 'djangoMain/send.html', context)


def succsess(request):
    asd = Bio.objects.all()
    context = {
        'asd': asd,
    }
    return render(request, 'djangoMain/succsess.html', context)



def history(request):
    asd = Bio.objects.all()
    context = {
        'asd': asd,
    }
    return render(request, 'djangoMain/history.html', context)

