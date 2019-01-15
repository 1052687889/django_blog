from django.shortcuts import render
from django.views import View
from django.shortcuts import render
# Create your views here.
from django.contrib.auth import authenticate,login
from django.contrib.auth.hashers import make_password

from django.http import HttpResponseRedirect
from django.urls import reverse
from apps.users.models import UserProfile
from .forms import LoginForm,RegisterForm
from apps.utils.email_send import send_register_email

class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        return render(request, 'register.html', {'register_form': register_form})

    def post(self,request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            username = request.POST.get('username','')
            user = UserProfile.objects.filter(username=username).all()
            if user:
                return render(request, 'register.html', {'msg': '用户 {0} 已存在'.format(username),'register_form':register_form})
            email = request.POST.get('email','')
            password = request.POST.get('password','')
            surepassword = request.POST.get('surepassword','')
            if password != surepassword:
                return render(request, 'register.html', {'msg': '两次密码输入不一致','register_form':register_form})
            user_profile = UserProfile()
            user_profile.username = username
            user_profile.email = email
            user_profile.password = make_password(password)
            user_profile.save()
            send_register_email(email,'register')
        return render(request, 'register.html',{'register_form':register_form})

class LoginView(View):
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
                return HttpResponseRedirect(reverse("home"))
            else:
                return render(request, 'login.html', {"msg": '用户名或密码错误,登录失败'})

        return render(request, 'login.html',{"login_form":login_form})

