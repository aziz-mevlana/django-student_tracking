from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def login_request(request):
    if request.user.is_authenticated:#? Kullanici giris yapmis ise login paneline eriesemesin anasayfaya gitsin
        return redirect("home")
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "account/login.html", {
                "error": "Kullanıcı adı veya şifre hatalı"
            })
        
    return render(request, "account/login.html")

def register_request(request):
    if request.user.is_authenticated:#? Kullanici giris yapmis ise register paneline eriesemesin anasayfaya gitsin
        return redirect("home")
    
    if request.method == "POST":
        username = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]
        
        if password == repassword:
            if User.objects.filter(username=username).exists():
                return render(request, "account/register.html", 
                {
                    "error": "Email zaten alınmış",
                    "username" : username,
                })
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect("login")
        else:
            return render(request, "account/register.html", 
            {
                "error": "Şifreler eşleşmiyor",
                "username" : username,
            })
    
    
    
    return render(request, "account/register.html")

def logout_request(request):
    logout(request)
    return redirect("home")



def profile_request(request):
    return render(request, "account/profile.html")