from django.shortcuts import render, redirect
from models import Product

def index(request):
    context = {
        'products' : Product.objects.all()
    }
    return render(request, 'restful/index.html', context)

def show(request, id):
    context = {
        'product': Product.objects.get(id=id),
    }
    return render(request, 'restful/show.html', context)

def new(request):
    return render(request, 'restful/new.html')

def edit(request, id):
    context = {
        'product': Product.objects.get(id=id),
    }
    return render(request, 'restful/edit.html', context)

def create(request):
    Product.objects.create(name=request.POST['name'], description=request.POST['description'], price=request.POST['price'])
    return redirect('/')

def update(request, id):
    product = Product.objects.get(id=id)
    product.name = request.POST['name']
    product.description = request.POST['description']
    product.price = request.POST['price']
    product.save()
    return redirect('/')

def destroy(request, id):
    Product.objects.get(id=id).delete()
    return redirect('/')
