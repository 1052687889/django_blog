from django.shortcuts import render
from django.views import View
from django.shortcuts import render
# Create your views here.
from django.contrib.auth import authenticate,login
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import LoginForm

class register(View):
    def get(self,request):
        return render(request,'register.html')

    def post(self,request):
        username = request.POST
        print(username)
        return render(request, 'register.html')

class user_login(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username','')
            password = request.POST.get('password','')
            user = authenticate(username=user_name,password=password)
            if user is not None:
                login(request,user)
                print('login success')
                return HttpResponseRedirect(reverse("home"))

        return render(request, 'login.html')

