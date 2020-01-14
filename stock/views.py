from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.shortcuts import redirect, render, get_object_or_404

from .models import Tobacco
from .models import Food

from .forms import BillForm

@login_required
def tobacco_stock(request):
    tobaccos = Tobacco.objects.all()
    return HttpResponse(render(request, 'tobacco_stock.html', {"tobaccos" : tobaccos}))

@login_required
def food_stock(request):
    food = Food.objects.all()
    print(food[2].history.all())
    return HttpResponse(render(request, 'food_stock.html', {"food" : food}))

@login_required
def new_bill(request):
    if request.method == 'GET':
        form = BillForm()
        food = Food.objects.all()
        return HttpResponse(render(request, 'new_bill.html', {"form" : form, "food" : food}))
    else:
        form = BillForm(request.POST, request.FILES)

        if form.is_valid():
            new_bill = form.save(commit=False)
            new_bill.save()

            return redirect('home')

@login_required
def history(request, type, id):
    if type == '0':
        obj = get_object_or_404(Tobacco, id=id)
        return HttpResponse(render(request, 'history.html', {"obj" : obj}))
    elif type == '1':
        obj = get_object_or_404(Food, id=id)
        return HttpResponse(render(request, 'history.html', {"obj" : obj}))

    return HttpResponse('hi')
