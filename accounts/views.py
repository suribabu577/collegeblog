from django.shortcuts import render
from django.shortcuts import redirect
from .models import *
import datetime
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User,auth


now = datetime.datetime.now()
# Create your views here.
#request.session['name']="AnonymousUser"
def index(request):

    return render(request,'accounts/index.html')


def admin_login(request):
    if request.method == 'POST':
        name=request.POST.get('id')
        psw=request.POST.get('psw')
        user=authenticate(username=name,password=psw)
        if user is not None:
            login(request,user)
            return redirect(news_feed)
        else:
            print("invalid")
            return redirect(admin_login)

    return render(request,'accounts/login.html')



def post(request):
    print(request.user)
    if request.user.is_authenticated:
        if request.method == 'POST':
            img=request.FILES['file']
            text=request.POST.get('text')
            time=str(now.strftime("%Y-%m-%d %H:%M"))
            s=upload(mail=current_user,image=img,text=text,uploaded_at=time)
            s.save()
        return render(request, 'accounts/upload.html')
    else:
        print('fuck')
        return redirect(admin_login)


def associats(request):
    context={ }
    if request.method == 'POST':
        name=request.POST.get('id')
        psw=request.POST.get('psw')
        user=authenticate(username=name,password=psw)
        if user is not None:
            login(request,user)
            return redirect(ssnf)
        else:
            print("invalid")
            return redirect(associats)
    
    return render(request,'accounts/login.html')

def students(request):
    if request.method == 'POST':
        name=request.POST.get('id')
        psw=request.POST.get('psw')
        user=authenticate(username=name,password=psw)
        if user is not None:
            login(request,user)
            return redirect(snf)
        else:
            print("invalid")
            return redirect(students)
    return render(request,'accounts/login.html')


def add_student(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name=request.POST.get('name')
            number=request.POST.get('number')
            branch=request.POST.get('branch')
            roll=request.POST.get('roll')
            email=request.POST.get('email')
            psw=request.POST.get('password')
            if User.objects.filter(username=email).exists():
                print('student exists')
            else:
                s=students_regitser(name=name,phn=number,Branch=branch,RN=roll,idd=email,psw=psw)
                s.save()
                user=User.objects.create_user(username=name,password=psw)
                user.save()
                print('added')
        return render(request,'accounts/register.html')
    else:
        return redirect(admin_login)
    

def add_staff(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            name=request.POST.get('name')
            number=request.POST.get('number')
            branch=request.POST.get('branch')
            roll=request.POST.get('roll')
            email=request.POST.get('email')
            psw=request.POST.get('password')
            if User.objects.filter(username=email).exists():
                print('exists')
            else:
                s=staff_regitser(name=name,phn=number,Branch=branch,RN=roll,idd=email,psw=psw)
                s.save()
                user=User.objects.create_user(username=name,password=psw)
                user.save()
                print('ok')
        return render(request,'accounts/register.html')
    else:

         return redirect(admin_login)   
    



def staff_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            img=request.FILES['file']
            text=request.POST.get('text')
            time=str(now.strftime("%Y-%m-%d %H:%M"))
            s=upload(mail=current_user,image=img,text=text,uploaded_at=time)
            s.save()
        return render(request, 'accounts/staffpost.html')
    else:
        return redirect(associats)

def news_feed(request):
    if request.user.is_authenticated:    
        users=upload.objects.all().order_by("id").reverse()
        p=users[len(users)-1].image
        return render(request,'accounts/newsfeed.html',{'users':users})
    else:
        return redirect(admin_login)


def snf(request):
    if request.user.is_authenticated:
        users=upload.objects.all().order_by("id").reverse()
        p=users[len(users)-1].image
        return render(request,'accounts/studentnf.html',{'users':users})
    else:
        return render(students)
    

def ssnf(request):
    if request.user.is_authenticated:
        users=upload.objects.all().order_by("id").reverse()
        p=users[len(users)-1].image
        return render(request,'accounts/staffnf.html',{'users':users})
    else:
        return render(associats)
    

def logout_request(request):
    if request.user.is_authenticated:
        logout(request)
        messages.info(request, "Logged out successfully!")
        return redirect(index)
    else:
        return render(index)









def management(request):

    return render(request,'accounts/management.html')


def cse(request):
    return render(request,'accounts/cse.html')


def ece(request):

    return render(request,'accounts/ece.html')


def eee(request):

    return render(request,'accounts/eee.html')


def it(request):

    return render(request,'accounts/it.html')


def civil(request):

    return render(request,'accounts/civil.html')


def mech(request):

    return render(request,'accounts/mech.html')

def hod(request):

    return render(request,'accounts/hod.html')

def af(request):

    return render(request,'accounts/af.html')

def la(request):

    return render(request,'accounts/la.html')
