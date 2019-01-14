from django.shortcuts import render
from django.views import View
from django.shortcuts import render
# Create your views here.

class register(View):
    def get(self,request):
        return render(request,'register.html')

    def post(self,request):
        username = request.POST
        print(username)
        return render(request, 'register.html')

class login(View):
    def get(self,request):
        return render(request,'register.html')