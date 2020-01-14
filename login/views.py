from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.shortcuts import redirect, render, get_object_or_404


def login_view(request):
    if request.method == 'GET':
        return HttpResponse('Error.')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse('Error. User hasn\'t logged')

@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

def index(request):
    if request.user.is_authenticated:
        return HttpResponse(render(request, 'index_auth.html'))

    return HttpResponse(render(request, 'index_login.html'))