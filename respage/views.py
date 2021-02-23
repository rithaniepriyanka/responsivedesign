from django.shortcuts import render

# Create your views here. 

def productsresponsive(request):
    context = {}
    return render(request, 'respage/productsresponsive.html', context)

def homeresponsive(request):
    context = {}
    return render(request, 'respage/homeresponsive.html', context)

def peopleresponsive(request):
    context = {}
    return render(request, 'respage/peopleresponsive.html', context) 

def contactusresponsive(request):
    context = {}
    return render(request, 'respage/contactusresponsive.html', context) 