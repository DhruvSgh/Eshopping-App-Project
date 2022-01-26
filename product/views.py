from django.shortcuts import render,redirect
from .models import Product,Customer
from django.contrib.auth.models import User,auth
from django.contrib import messages
def index(request):
    product=Product.objects.all()
    return render(request,'index.html',{'products':product})
def register(request):
    if request.method=="POST":
        first_name=request.POST['fname']
        last_name=request.POST['lname']
        username=request.POST['uname']
        email=request.POST['email']
        password=request.POST['pwd']
        address=request.POST['address']
        mobile=request.POST['mobile']
        if User.objects.filter(username=username).exists():
            print("already taken")
        else:
            user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
            user.save()
            c=Customer(user.id,address,email)
            c.save()
            auth.login(request,user)
            return redirect("/")

    else:
        return render(request,'register.html')
def logout(request):
    auth.logout(request)
    product=Product.objects.all()
    return render(request,'index.html',{'products':product})
def login(request):
    if request.method=="POST":
        username=request.POST['uname']
        password=request.POST['password']
        if auth.authenticate(username=username,password=password):
            user=User.objects.get(username=username)
            auth.login(request,user)
            return redirect("/")
        else:
            messages.info(request,"invalid id and password")
            return redirect("/login")
        
    else:
        return render(request,'login.html')
def check(request):
    return render(request,"check.html")