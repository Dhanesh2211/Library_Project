from django.shortcuts import render,HttpResponse,redirect

# Create your views here.

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

from .models import admin_signup,book_details


def index(request):
    return render(request,"index.html")


def dashboard(request):
     result=book_details.objects.all()
     return render(request,"dashboard.html",{'book_details':result}) 
     
   


def signup(request):
    return render(request,"signup.html")


def save_data(request):
    if request.method=="POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        passw=request.POST['passw']
        au=User.objects.create_user(first_name=fname,last_name=lname,username=email,password=passw)
        au.save()#Inserting Data

        app=admin_signup(au=au,admin_address=request.POST['admin_address'],admin_number=request.POST['admin_number'])
        app.save()
        return render(request,"index.html")
    
    return render(request,"index.html")     
   


def log(request):
    if request.method=="POST":
        email=request.POST["email"]
        passw=request.POST["passw"]
        
        au=authenticate(username=email,password=passw)
        if au:
            login(request,au) #Session Start
            return redirect("/dashboard")  
        else:
            return HttpResponse("Login Fail")



def admin_logout(request):
    logout(request) #Logout Session
    return render(request,"index.html")     


def add_book(request):
    if request.method=="POST":
        Book_Name=request.POST['Book_Name']
        Book_Image=request.FILES['Book_Image']
        Book_Description=request.POST['Book_Description']
        Book_date=request.POST['Book_date']
        app=book_details(Book_Name=Book_Name,Book_Image=Book_Image, Book_Description=Book_Description, Book_date=Book_date)
        app.save()#Inserting Data
        return redirect('dashboard')

def book_delete(request):
    id=request.GET["id"]
    book_details.objects.filter(id=id).delete()  #Delete Query
    return redirect("/dashboard")

def book_edit(request):
    id=request.GET["id"]
    data=book_details.objects.filter(id=id)
    return render(request,"edit.html",{'data':data})

def book_update(request):
    
    if request.method=="POST":
        id=request.POST['id']
        Book_Name=request.POST['Book_Name']
        Book_Description=request.POST['Book_Description']
        Book_date=request.POST['Book_date']
        #update

        app=book_details.objects.filter(id=id).update(Book_Name=Book_Name,Book_Description=Book_Description,Book_date=Book_date) 


        return redirect("dashboard")
    else:
        return HttpResponse("Fail")