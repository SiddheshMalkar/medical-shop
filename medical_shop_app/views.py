from django.shortcuts import render
from django.http import HttpResponse,request
from .models import *
from .forms import *
import logging

def home(request):
    return render(request, 'home.html')

def add_customer(request):
    if request.method == 'POST':
        form = saveCustomer(request.POST)
        if form.is_valid():
            print("done1")
            form.save()
            print("done2")
        else:
            print("error")
    else:
        form = saveCustomer()


    customers = Customer.objects.all()
    context = {'customers':customers}
    return render(request, 'add_customer.html',context)
    #return render(request, 'add_customer.html')


def add_medicine(request):
    if request.method == 'POST':
        form = saveMedicine(request.POST)
        if form.is_valid():
            print("done1")
            form.save()
            print("done2")
        else:
            print("error")
    else:
        form = saveMedicine()
    return render(request, 'add_medicine.html')

def add_stock(request):
    if request.method == 'POST':
        form = saveStock(request.POST)
        if form.is_valid():
            #logger.info('hi!')
            t = Medicine.objects.get(mid=form.data['mid'])
            t.stock = form.data['stock']  # change field
            t.save() # this will update only
        else:
            print("error in update")
    else:
        form = saveStock()

    

    medicines = Medicine.objects.all()
    context = {'medicines':medicines}
    return render(request, 'add_stock.html',context)
    #return render(request, 'add_stock.html')