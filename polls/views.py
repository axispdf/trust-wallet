import time
from django.http import HttpResponseRedirect
from django.shortcuts import render
from polls.models import *
from polls.forms import *



def index(request): 
    if not request.user.is_authenticated:
        return render(request, 'djangoMain/main.html')
    else:
        user = User
        bio = Bio.objects.filter(users=request.user)
        print(request.user) 
        context = {
            'user': user,
            'bio': bio
        }
        return render(request, 'djangoMain/index.html', context)




def send(request):
    if not request.user.is_authenticated:
        return render(request, 'djangoMain/main.html')
    else:
        sec = time.time()
        struct = time.localtime(sec)
        bio = Bio.objects.filter(users=request.user)
        form = ModelesFormClass(request.POST)
        lastword = bio.order_by('balance')[0].balance
        if form.is_valid():
            a = form.cleaned_data.get('amount')
            s = form.cleaned_data.get('adress')
            if lastword > int(a):
                histor = History(user=request.user , adress=s , amount=a , crypto='USDT' , datatimes=time.strftime('%d.%m.%Y %H:%M', struct))
                histor.save()
                action = int(lastword) - int(a)
                lastaction = str(action)
                bio.delete()
                fixamount = Bio(users=request.user, balance=lastaction)
                fixamount.save()
            else: 
                return HttpResponseRedirect("/")

        else:
            error = 'Форма была не правмильная'
            print(error)
        context = {
            'form': form,
            'bio': bio, 
        }
        return render(request, 'djangoMain/send.html', context)


def testform(request):
    if not request.user.is_authenticated:
        return render(request, 'djangoMain/main.html')
    else:
        bio = Bio.objects.filter(users=request.user)
        context = {
            'bio': bio, 
            }
        return render(request, 'djangoMain/main.html', context)


def succsess(request):
    if not request.user.is_authenticated:
        return render(request, 'djangoMain/main.html')
    else:
        bio = Bio.objects.filter(users=request.user)
        context = {
            'asd': bio,
        }
        return render(request, 'djangoMain/succsess.html', context)



def history(request):
    bio = Bio.objects.filter(users=request.user)
    history = History.objects.filter(user=request.user)
    context = {
        'history': history,
        'asd': bio,
    }
    return render(request, 'djangoMain/history.html', context)

