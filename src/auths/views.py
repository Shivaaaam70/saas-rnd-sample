from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from django.contrib.auth import get_user_model
user = get_user_model()

# Create your views here.

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if all([username, password]):
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("Login Here........")
                return redirect("/")
    return render(request, "auth/login.html", {})


def register_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        try:
            user.objects.create_user(username, email=email, password=password)
        except:
            pass
        
    return render(request, "auth/register.html", {})
             
            
            
            
