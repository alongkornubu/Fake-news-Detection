from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,UsernameField
from django.contrib.auth.models import User
from .models import *

# label = "ชื่อผู้ใช้งาน"
# label = "รหัสผ่าน" 
# label = "ยืนยันรหัสผ่าน" 

class Registerform(UserCreationForm):
    username = forms.CharField(label="ชื่อผู้ใช้งาน", widget=forms.TextInput
    (attrs={'class':'rounded-sm border-2 px-4 py-3 mt-3 focus:outline-none bg-white w-full'}))
    password1 = forms.CharField(label="รหัสผ่าน", widget=forms.PasswordInput
        (attrs={'class':'rounded-sm border-2 px-4 py-3 mt-3 focus:outline-none bg-white w-full'}))
    password2 = forms.CharField(label="ยืนยันรหัสผ่าน", widget=forms.PasswordInput
        (attrs={'class':'rounded-sm border-2 px-4 py-3 mt-3 focus:outline-none bg-white w-full'}))

    class Meta:
        model = User
        fields = {'username'}

class Loginform(AuthenticationForm):
    username = UsernameField(label="ชื่อผู้ใช้",widget= forms.TextInput(attrs={'class':'rounded-sm px-4 py-3 mt-3 focus:outline-none bg-gray-100 w-full'}))
    password = forms.CharField(label="รหัสผ่าน",strip=False,widget=forms.PasswordInput(attrs={'class':'rounded-sm px-4 py-3 mt-3 focus:outline-none bg-gray-100 w-full'}))


class news(forms.ModelForm):
    class Meta:
        model = New
        fields = ['title' , 'text' ,'tag', 'image']
        
class detect_fake_news(forms.Form):
    class Meta:
        text = forms.CharField(label='ข่าว', max_length=500)
