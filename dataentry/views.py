from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth import authenticate
from django.utils import timezone
from .models import Customer
import datetime



# Create your views here.

def register(request):
    if request.method=="POST":
        username=request.POST.get('username', '')
        email=request.POST.get('email', '')
        password=request.POST.get('password', '')
        age=request.POST.get('age', '')

        if User.objects.filter(username=username).exists():
            messages.info(request,'Mobile Number is already taken')
            return redirect('register')
        elif User.objects.filter(email=email).exists():
            messages.info(request,'Email is already taken')
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, password=password, email=email)
            user.save();
            messages.info(request,'Thanks gor signing in, User Created')
            return redirect('login')

    return render(request, 'register.html')


def login(request):
    if request.method=="POST":
        username=request.POST.get('username', '')
        password=request.POST.get('password', '')
    
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            
            print(username)
            return redirect('entryForms')
        else:
            messages.info(request,'Invalid Credentials, Check your Mobile Number and Password')
            return redirect('login')
    
    else:
        return render(request,'login.html')
    
def entryForms(request):
    # param={}
    # check = False
    # print(request)
    name=request.POST.get('name', '')
    age=request.POST.get('age', '')
    gender=request.POST.get('gender', '')
    familyMembers=request.POST.get('familyMembers', '')
    dob=request.POST.get('dob', '')
    doa=request.POST.get('doa', '')

    creationDate = datetime.date.today()
    # for debugging (breakpoint in server)
    # import pdb;pdb.set_trace()
    
        

    if request.method=="POST":
        custms = Customer(name=name, age=age, gender=gender, family_members=familyMembers, dob=dob, doa=doa, user=request.user)
        custms.save()
        # check=True
    else:
    
    # for debugging (breakpoint in server)
        # import pdb;pdb.set_trace()
    
        custms = Customer.objects.filter(created_ts= creationDate, user=request.user).first()
    
    return renderEntryForm(request, custms)

def renderEntryForm(request, custms):
    
    param = {'custms':custms}
    return render(request, 'entryForms.html', param)

def updateForm(request):
    name=request.POST.get('name', '')
    age=request.POST.get('age', '')
    gender=request.POST.get('gender', '')
    familyMembers=request.POST.get('familyMembers', '')
    dob=request.POST.get('dob', '')
    doa=request.POST.get('doa', '')

    creationDate = datetime.date.today()
    if request.method=="POST":
        custms = Customer.objects.filter(created_ts= creationDate, user=request.user).first()
        if custms:
            custms.name = name
            custms.age = age
            custms.gender = gender
            custms.familyMembers = familyMembers
            custms.dob = dob
            custms.doa = doa
            custms.save()

    return renderEntryForm(request, custms)


def logout(request):
    auth.logout(request)
    return redirect('/')

    


    