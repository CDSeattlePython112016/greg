from django.shortcuts import render

def index(request):
    return render(request,'disappearninja/index.html')

def all(request):
    context = {
        'group':True
    }
    return render(request,'disappearninja/ninja.html', context)

def ninja(request, color):
    print'getting to ninja method'
    context = {
        'group':False,
        'color':color
    }
    return render(request, 'disappearninja/ninja.html', context)
