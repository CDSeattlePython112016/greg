from django.shortcuts import render, redirect

def index(request):
    return render(request,'dojosurvey/index.html')

def process(request):
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['languages'] = request.POST['languages']
    request.session['comments'] = request.POST['comments']
    return redirect('/result')

def result(request):
    return render(request, 'dojosurvey/result.html')
