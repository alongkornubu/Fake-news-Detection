from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.views.generic import View

from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

from .forms import *
from .models import *

def home(request):
    return render(request, 'news/index.html')

def login(request):
    return render(request, 'news/login.html')

def follow(request):
    # new = AddNew.objects.all()
    new = AddNew.objects.filter(tag="โควิด 19")
    return render(request,'news/follow.html',{'new': new} )

class SignupView(View):
    def get(self,request):
        fm = Registerform()
        return render(request,'news/signup.html',{'form':fm})
    def post(self,request):
        fm = Registerform(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('detect-news')
        else:
            return render(request,'news/signup.html',{'form':fm})
    
    
class LoginView(View):
    def get(self,request):
        fm = Loginform()
        return render(request,'news/login.html',{'form':fm})
    def post(self,request):
        fm = Loginform(request,data= request.POST)
        if fm.is_valid():
            username = fm.cleaned_data['username']
            password = fm.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('follow')
            else:
                return render(request, 'news/login.html',{'form':fm}) 
            
        else:
            return render(request, 'news/login.html',{'form':fm}) 
        


def news_feedback(request):

    context = {}

    if request.method == 'POST':
        data = request.POST.copy()
        name = data.get('name')
        fakeortrue = data.get('fakeortrue')
        detail = data.get('detail')
        print(name,detail , fakeortrue)

        if name == '' or fakeortrue == '':
            context['status'] = 'alert'
            return render(request, 'news/feedback.html',context)
        
        test = Feedback()
        test.name = name
        test.fakeortrue = fakeortrue
        test.detail = detail
        test.save()
        context['status'] = ['success']

    return render(request, 'news/feedback.html',context)





