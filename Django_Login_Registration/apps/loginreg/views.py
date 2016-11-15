from django.shortcuts import render, redirect
from django.contrib import messages
from models import User

def index(request):
    # User.userMgr.all().delete()
    users = User.userMgr.all()
    return render(request, 'loginreg/index.html')

def login(request):
    resp = User.userMgr.login(request.POST)
    if resp['logged']:
        messages.success(request, 'You have successfully logged in.')
        return redirect('/success')
    else:
        messages.error(request, 'Email/Password does not match.')
    return redirect('/')

def register(request):
    resp = User.userMgr.register(request.POST)
    if resp['added']:
        if 'user' not in request.session:
            request.session['userid'] = resp['new_user'].id
            messages.success(request, 'You have successfully registered.')
        return redirect('/success')
    else:
        for error in resp['errors']:
            messages.error(request, error)
        return redirect('/')

def success(request):
    context = {
        'user': User.userMgr.get(id=request.session['userid'])
    }
    return render(request, 'loginreg/success.html', context)
