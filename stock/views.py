from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.shortcuts import redirect, render, get_object_or_404

from .models import Tobacco, BillTobacco
from .models import Food
from .models import Bill
from .forms import BillForm

@login_required
def tobacco_stock(request):
    tobaccos = Tobacco.objects.all()
    return HttpResponse(render(request, 'tobacco_stock.html', {"tobaccos" : tobaccos}))

@login_required
def food_stock(request):
    food = Food.objects.all()
    return HttpResponse(render(request, 'food_stock.html', {"food" : food}))

@login_required()
def new_bill(request):
    if request.method == 'GET':
        form = BillForm()
        food = Food.objects.all()
        tobaccos = Tobacco.objects.all()
        return HttpResponse(render(request, 'new_bill.html', {"form" : form, "food" : food, "tobaccos": tobaccos}))
    else:
        form = BillForm(request.POST, request.FILES)
        print(request.POST)
        new_bill = Bill(id_user=request.POST['id_user'], sum=request.POST['total_sum'])
        new_bill.save()
        for i in range(1, int(request.POST['hookah_count']) + 1):
            print(request.POST['tobacco' + str(i)])
            curr_tobacco = Tobacco.objects.get(id=int(request.POST['tobacco' + str(i)]))
            delta = int(request.POST['count_tobacco' + str(i)])
            curr_tobacco.weight -= delta
            curr_tobacco.save()
        for i in range(1, int(request.POST['food_count']) + 1):
            print(request.POST['food' + str(i)])
            curr_food = Food.objects.get(id=int(request.POST['food' + str(i)]))
            delta = int(request.POST['count_food' + str(i)])
            curr_food.count -= delta
            curr_food.save()
        return redirect('home')

@login_required()
def delivery(request):
    if request.method == 'GET':
        food = Food.objects.all()
        tobaccos = Tobacco.objects.all()
        return HttpResponse(render(request, 'delivery.html', {"food" : food, "tobaccos": tobaccos}))
    else:
        print(request.POST)
        for i in range(1, int(request.POST['hookah_count']) + 1):
            print(request.POST['tobacco' + str(i)])
            curr_tobacco = Tobacco.objects.get(id=int(request.POST['tobacco' + str(i)]))
            delta = int(request.POST['count_tobacco' + str(i)])
            curr_tobacco.weight += delta
            curr_tobacco.save()

        for i in range(1, int(request.POST['food_count']) + 1):
            print(request.POST['food' + str(i)])
            curr_food = Food.objects.get(id=int(request.POST['food' + str(i)]))
            delta = int(request.POST['count_food' + str(i)])
            curr_food.count += delta
            curr_food.save()

        for i in range(1, int(request.POST['newf_number']) + 1):
            name = request.POST['newf' + str(i)]
            number = request.POST['newf_count' + str(i)]
            price = request.POST['newf_cost' + str(i)]
            if int(number) > 0:
                curr_food = Food.objects.create(name=name, count=number, cost=price)
                curr_food.save()

        for i in range(1, int(request.POST['newt_number']) + 1):
            name = request.POST['newt' + str(i)]
            number = request.POST['newt_count' + str(i)]
            price = request.POST['newt_cost' + str(i)]
            if int(number) > 0:
                curr_tobacco = Tobacco.objects.create(name=name, weight=number, cost=price)
                curr_tobacco.save()

        return redirect('home')
