import urllib
from django.views import View
from django.shortcuts import render
# Create your views here.
from django.contrib.auth import authenticate,login
from django.contrib.auth.hashers import make_password
from django.http import HttpResponseRedirect
from django.urls import reverse
from apps.users.models import UserProfile,EmailVerifyRecord
from .forms import LoginForm,RegisterForm
from apps.utils.email_send import send_register_email
# from apps.Article.models import Article
from django_blog.genfunc import get_top_data


class RegisterView(View):
    def get(self,request):
        register_form = RegisterForm()
        context = get_top_data(request)
        context.update({'register_form': register_form})
        return render(request, 'register.html', context=context)

    def post(self,request):
        context = get_top_data(request)
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
                context.update({'msg': '两次密码输入不一致','register_form':register_form})
                return render(request, 'register.html', context=context)
            user_profile = UserProfile()
            user_profile.username = username
            user_profile.email = email
            user_profile.password = make_password(password)
            user_profile.is_active = False
            user_profile.save()
            send_register_email(email,username,'register')
            context.update({'email_msg': '注册邮件已发送，请注意查收.', 'register_form': register_form})
            return render(request, 'register.html', context=context)
        context.update({'register_form':register_form})
        return render(request, 'register.html',context=context)

class LoginView(View):
    def get(self,request):
        context = get_top_data(request)
        return render(request,'login.html',context=context)

    def post(self,request):
        login_form = LoginForm(request.POST)
        context = get_top_data(request)
        if login_form.is_valid():
            user_name = request.POST.get('username','')
            password = request.POST.get('password','')
            user = authenticate(username=user_name,password=password)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect(reverse("home"))
            else:
                context.update({"msg": '用户名或密码错误,登录失败'})
                return render(request, 'login.html', context=context)

        context.update({"login_form":login_form})
        return render(request, 'login.html',context=context)


class ActiveUserView(View):
    def get(self,request):
        username = request.GET.get("username","")
        code = request.GET.get("code","")
        context = get_top_data(request)
        if username and code:
            username = urllib.parse.unquote(username)
            obj = EmailVerifyRecord.objects.filter(username=username).filter(code=code).first()
            if obj:
                user = UserProfile.objects.filter(email=obj.email).filter(username=obj.username).first()
                user.is_active = True
                user.save()
                context['username'] = username
                context['email'] = user.email
                context['msg'] = '激活成功!!!'
                return render(request,'email_active.html',context)

        context['username'] = username
        context['msg'] = '激活失败!!!'
        return render(request, 'email_active.html', context=context)









