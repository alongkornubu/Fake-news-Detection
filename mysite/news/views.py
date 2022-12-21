from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# api newsapi
from newsapi import NewsApiClient

# pythainlp
from pythainlp import word_tokenize

from .forms import *
from .models import *

def home(request):
    return render(request, 'news/index.html')

def login(request):
    return render(request, 'news/login.html')

def follows(request):
    return render(request, 'news/follows.html')

def new(requests):
    return render(requests, 'news/addnew.html')


def follow(request):
    # new = AddNew.objects.filter(tag="โควิด 19")
    # new = AddNew.objects.get(id=14)
    new = New.objects.all()
    tag = []
    for i in new:
        if i.tag not in tag:
            tag.append(i.tag)
        else:
            continue
    return render(request,'news/follow.html',{'new': new,'tag':tag})

class SignupView(View):
    def get(self,request):
        form = Registerform()
        return render(request,'news/signup.html',{'form':form})
    def post(self,request):
        form = Registerform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            return render(request,'news/signup.html',{'form':form})
    
    
class LoginView(View):
    def get(self,request):
        form = Loginform()
        return render(request,'news/login.html',{'form':form})
    def post(self,request):
        form = Loginform(request,data= request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('follow')
            else:
                return render(request, 'news/login.html',{'form':form}) 
            
        else:
            return render(request, 'news/login.html',{'form':form}) 
        


def news_feedback(request):

    context = {}

    if request.method == 'POST':
        data = request.POST.copy()
        name = data.get('name')
        fakeortrue = data.get('fakeortrue')
        detail = data.get('detail')
        link = data.get('link')
        # print(name,detail , fakeortrue ,link)

        if name == '' or fakeortrue == '':
            context['status'] = 'alert'
            return render(request, 'news/feedback.html',context)
        
        test = Feedback()
        test.name = name
        test.fakeortrue = fakeortrue
        test.detail = detail
        test.link = link
        test.save()
        context['status'] = ['success']

        
    return render(request, 'news/feedback.html',context)





