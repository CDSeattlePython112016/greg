from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Email
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

def index(request):
    return render(request, 'emailvalidation/index.html')

def submit(request):
    print request
    if Email.emailManager.validate_add(request, request.POST['email']):
        context = {
            'emails' : Email.emailManager.all()
        }
        return render(request, 'emailvalidation/success.html', context)
    return redirect('/')

# def remove(request, id):
#     print request
#     Email.emailManager.remove(request, id)
#     context = {
#         'emails' : Email.emailManager.all()
#     }
#     return render(request, 'emailvalidation/success.html', context)
