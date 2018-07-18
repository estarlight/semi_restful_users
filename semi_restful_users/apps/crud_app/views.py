from django.shortcuts import render, redirect, reverse
from .models import *

# Create your views here.
def index(request):
    # request.session['last_visited'] = 'index'

    context = {
        "all_users": User.objects.all(),
    }

    return render(request, 'index.html', context)

def new(request):

    return render(request, 'new.html')

def create(request):

    created_user = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'])


    return redirect(reverse('show', kwargs={'id_num':created_user.id} ))

def show(request, id_num):

    # request.session['last_visited'] = 'show'

    context ={
        "user": User.objects.get(id=id_num),
    }

    return render(request, 'show.html', context)

def edit(request, id_num):

    context = {
        "user": User.objects.get(id=id_num)
    }

    return render(request, 'edit.html', context)

def update(request, methods='POST'):

    # id = request.POST['user_id']

    print(request.POST)

    user = User.objects.get(id=request.POST['user_id'])

    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.email = request.POST['email']
    user.save()

    return redirect(reverse('show', kwargs={'id_num': request.POST['user_id']} ))

def destroy(request, id_num):

    user = User.objects.get(id=id_num)
    user.delete()

    return redirect(reverse('index'))