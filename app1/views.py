from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render,HttpResponse

from .models import Profile


def home(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        name=request.POST.get('name')
        user=User.objects.create_user(username=username,password=password,first_name=name)
        user.save()
    return render(request,'home.html')

def login(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print(user.id)
            return render(request,'login.html',{'user_id':user.id})

def profile(request):
    if request.method=="POST":
        id=request.POST.get('id')
        user1=User.objects.get(id=id)
        name = request.POST.get('name')
        city = request.POST.get('city')
        age = request.POST.get('age')
        if Profile.objects.get(user=user1):
            profile=Profile.objects.get(user=user1)
            print(profile)
            profile.name=name
            profile.city=city
            profile.age=age
            profile.save()

        else:
            profile=Profile(user=user1,name=name,city=city,age=age)
            profile.save()
        data = profile.values()
        return render(request,'profile.html', {'id':user1.username+'data saved','user_id':id,'data':data})
    return render(request,'profile.html')
