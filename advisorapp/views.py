import respond as respond
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import  authenticate, login,logout
from django.contrib.auth.decorators import  login_required
from advisorapp.models import advdisplay
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import  authenticate,login,logout
from advisorapp.models import addadvisor
from advisorapp.models import Bookadvisor1
from advisorapp.models import users
from .forms import CreateUserForm, CreateAdvisors, FilterForm

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('userdashboard')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                if user.is_superuser:
                    login(request,user)
                    return redirect('addadvisor')
                else:
                    if user is not None:
                        login(request,user)
                        return redirect('userdashboard')
        context = {}
        return render(request,'booking/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

# @login_required(login_url='login')
def addadvisorPage(request):
    if request.method == 'POST':
        addadv = addadvisor()
        addadv.advname = request.POST.get('advname')

        if len(request.FILES) != 0:
            addadv.profilepic = request.FILES['profilepic']
            addadv.save()
    return render(request, 'booking/addadvisor.html')

#@login_required(login_url='login')
def bookingPage(request):
    return render(request,'booking/booking_info.html')

  def mainadminPage(request):
    return render(request,'booking/mainadmin.html')

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('userdashboard')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        context={'form':form}
        return render(request,'booking/register.html')

@login_required(login_url='login')
def userdashboardPage(request):
    displayaddadvisor = addadvisor.objects.all()
    displayadvisor = advdisplay.objects.all()
    total_booked = displayadvisor.count()
    context = {'displayaddadvisor':displayaddadvisor,'displayadvisor':displayadvisor,'total_booked':total_booked}
    return render(request,'booking/userdashboard.html',context)

def profilePage(request):
    context={}
    return render(request,'booking/profilesetting.html',context)

def bookinginfoPage(request):
    displayadvisor = advdisplay.objects.all()
    context = { 'displayadvisor': displayadvisor}
    return render(request,'booking/booking_info.html',context)

def displayPage(request):
    displayaddadvisor = addadvisor.objects.all()

    if request.method=='POST':
        if request.POST.get('bookpeople'):
            savevalue=advdisplay()
            savevalue.bookpeople=request.POST.get('bookpeople')
            savevalue.save()
            return render(request, 'booking/listofadvisors.html',{'savevalue':savevalue})

    context = {'displayaddadvisor':displayaddadvisor}
    return render(request,'booking/listofadvisors.html',context)
