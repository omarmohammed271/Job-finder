from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse

# Create your views here.
def login_view(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if username and password:
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('home')
            
        
            
    return render(request,'accounts/login.html')

def register(request):
    if request.method=='POST':
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        username = email.split('@')[0]
        if password1==password2:
            try:
                is_user = User.objects.get(username=username)
            
                return HttpResponse('This Email Already Have Account')
            except:
                user = User.objects.create_user(username=username,email=email,password=password1)
                login(request,user)
                return redirect('home')
    return render(request,'accounts/register.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:login')
