from django.shortcuts import render, redirect
from django.contrib import messages
from models import User
from django.core.urlresolvers import reverse

def index(request):
    # User.objects.all().delete()
    users = User.objects.all()
    return render(request, 'loginreg/index.html')

def login(request):
    resp = User.objects.login(request.POST)
    if resp['logged']:
        messages.success(request, 'You have successfully logged in.')
        return redirect(reverse('login:success'))
    else:
        messages.error(request, 'Email/Password does not match.')
    return redirect(reverse('login:index'))

def register(request):
    resp = User.objects.register(request.POST)
    if resp['added']:
        if 'user' not in request.session:
            request.session['userid'] = resp['new_user'].id
            messages.success(request, 'You have successfully registered.')
        return redirect(reverse('login:success'))
    else:
        for error in resp['errors']:
            messages.error(request, error)
        return redirect(reverse('login:index'))

def success(request):
    context = {
        'user': User.objects.get(id=request.session['userid'])
    }
    return render(request, 'loginreg/success.html', context)
