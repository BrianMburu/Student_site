from django import forms
from megapp.models import UserProfileInfo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model = User
        fields = ('username','birth_date','email','password')
class UserProfileInfoForm(forms.ModelForm):
     class Meta():
         model = UserProfileInfo
         fields = ('course','profile_pic')