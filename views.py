from django.shortcuts import render
from django.contrib.auth.models import User 
from django.contrib.auth import login, logout, authenticate
from random import*
from django.core.mail import send_mail

def uhome(request):
    if request.user.is_authenticated:
        return redirect("uwelcome")
    else:
        if request.method =="POST":
            un = request.POST.get("un")
            pw = request.POST.get("pw")
            usr = authenticate(username=un,password=pw)
            if usr is None:
                return render(request,"uhome.html",{"msg":"Invalid username / password"})
            else:
                login(request,usr)
                return redirect("uwelcome")
        else:
            return render(request,"uhome.html") 

def usignup(request):

    if request.user.is_authenticated:
        return redirect("uwelcome")
    else:
        if request.method=="POST":
            un = request.POST.get("un")
            try:
                usr = User.objects.get(username=un)
                return render(request, "usignup.html", {"msg":"email aready registered"})
            except User.DoesNotExist:
                pw = randint(1000,9999)
                print(pw)
                usr=User.objects.create_user(username=un, password = str(pw))
                usr.save()
                subject = "Welcome To kamal Classes"
                text = "ur password is " + str(pw)
                from_email= "test.sumit.2march23@gmail.com"
                to_email= [str(un)]
                send_mail(subject,text,from_email,to_email)
                return redirect("home")
        else:
            return render(request, "usignup.html")
        
def uwelcome(request):

    if request.user.is_authenticated:
        return render(request, "uwelcome.html")
    else:
        return redirect("uhome")

def ulogout(request):
    logout(request) 
    return redirect("uhome")
