from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth import login as auth_login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

#ML
import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.metrics import accuracy_score, confusion_matrix

#pythainlp
from pythainlp.corpus import thai_stopwords 
stop_words = thai_stopwords()
from pythainlp.tokenize import word_tokenize 

# อ่านโมเดล
model = pickle.load(open('/mysite/model.pkl', 'rb'))
dataframe = pd.read_csv('./data/Data_news.csv')
x = dataframe['text']
y = dataframe['label']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)


from .forms import *
from .models import *

def text_tokenizer(text):
    terms = [k.strip() for k in word_tokenize(text) if len(k.strip()) > 0 and k.strip()] 
    return [t for t in terms if len(t) > 0 or t is not None]
def text_processor(text):
    return text
    
stop_words = [t.encode('utf-8') for t in list(thai_stopwords())]
tfidf_vectors = TfidfVectorizer(
    tokenizer = text_tokenizer,
    preprocessor = text_processor,
    ngram_range=(2,3),
    stop_words=stop_words,
    max_features=3_000        
)    

def detect(Data_News):
    input_data = [Data_News]
    vectorized_input_data = tfidf_vectors.transform(input_data)
    prediction = model.predict(vectorized_input_data)
    return prediction

def detect_news(request):
    if request.method == 'POST':
        data = request.POST.copy()
        text = data.get('text')
        pred = detect(text)
        # print(text)
        
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
        text = data.get('text')
        link = data.get('link')
        # print(name,text , fakeortrue ,link)

        if name == '' or fakeortrue == '':
            context['status'] = 'alert'
            return render(request, 'news/feedback.html',context)
        
        test = Feedbacks()
        test.name = name
        test.fakeortrue = fakeortrue
        test.text = text
        test.link = link
        test.save()
        context['status'] = ['success']

        
    return render(request, 'news/feedback.html',context)





