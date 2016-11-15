from django.shortcuts import render
from random import choice
from string import ascii_uppercase

def index(request):
    word = ''.join(choice(ascii_uppercase) for i in range(14))
    request.session['rndword'] = word
    if 'counter' not in request.session:
        request.session['counter'] = 1
    else:
        request.session['counter'] += 1
    return render(request,'rndwordgen/index.html')
