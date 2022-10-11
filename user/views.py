from http.client import HTTPResponse
from django.shortcuts import render, redirect
from twilio.rest import Client
from django.contrib import messages
from django.contrib.auth.models import User
from user.models import Userprofile
from django.contrib.auth import login as auth_login 
from django.contrib.auth import authenticate,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.

  
def register(request):
    if request.user.is_authenticated:
      return redirect("/")
    if request.method == "POST":
        try:
            email = request.POST['email']
            User.objects.get(username = request.POST['email'])
            messages.error(request, f"The Email {email} is already taken. Try a unique Email.")
            return redirect ('/myaccount/register/')
        except User.DoesNotExist:
            fname = request.POST.get('fname')
            lname = request.POST.get('lname')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User(username=email, first_name=fname, last_name=lname)
            user.set_password(password)
            user.save()
            messages.success(request, f"Registration Successful. Welcome {fname} {lname}. Please Login to Proceed.")
            return redirect('/myaccount/login/') 
    else:
        return render(request,'register.html')
       

def login(request):
    if request.user.is_authenticated:
      return redirect("/")
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            auth_login(request,user)
            messages.success(request, f"Welcome back {user.username}.")
            return redirect('/myaccount/profile/')
        else:
            messages.error(request, f"Invalid Credentials. Login again.")
            return redirect('/myaccount/login/')
    else:               
        return render(request, "login.html") 

@login_required(login_url='login')
def editprofile(request):
    if request.method == "POST":
        first_name = request.POST.get('fname')
        last_name = request.POST.get('lname')
        username = request.POST.get('email')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        user = User.objects.get(id = request.user.id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.save()

        user_details = Userprofile.objects.get(id = request.user.userprofile.id)
        user_details.age = age
        user_details.gender = gender
        user_details.save()

        messages.success(request, f"Profile Details updated successfully.")
        return redirect('/myaccount/profile/') 
    else:
        return render(request,'update-profile.html')


def logout_user(request):
	logout(request)
	return redirect("/myaccount/login/")

@login_required(login_url='login')
def profile(request):
    user_id = request.user.id
    user=User.objects.filter(id=user_id).first()
    return render(request, "profile.html",{'user':user})   

@login_required(login_url='login')
def addprofile(request):
    if request.method == "POST":
        age = request.POST.get('age')
        gender = request.POST.get('gender')

        user_instance = Userprofile.objects.get(id = request.user.userprofile.id)
        user_details = user_instance(age=age, gender=gender)
        user_details.save()

        messages.success(request, f"Profile Details updated successfully.")
        return redirect('/myaccount/profile/') 
    else:
        return render(request,'update-profile.html')


'''@login_required(login_url='login')
def update_pic(request):
    if request.method == "POST":
        picture = request.File["picture"]

        user_profile = Userprofile.objects.get(id = request.user.userprofile.id)
        user_profile.picture = picture
        user_profile.save()

        messages.success(request, f"Profile Picture updated successfully.")
        return redirect('/profile/')
    return render(request, "update-picture.html") '''  