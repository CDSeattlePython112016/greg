from django.shortcuts import render, redirect
import datetime
from random import choice
from string import ascii_uppercase

def index(request):
    now = datetime.datetime.now()
    word = ''.join(choice(ascii_uppercase) for i in range(14))
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1
    context = {
    'now': now,
    'word': word,
    }
    return render(request, 'integrate/index.html', context)
