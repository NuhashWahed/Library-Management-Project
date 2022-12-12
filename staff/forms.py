from django import forms  
from .models import Book,IssueBook 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm 

class BookForm(forms.ModelForm):  
    class Meta:  
        model = Book  
        fields = "__all__" 
class IssueBookForm(forms.ModelForm):  
    class Meta:  
        model = IssueBook  
        fields = "__all__" 
class EditprofileForm(UserChangeForm):
    password=None
    class Meta:
        model=User
        fields=['email','first_name','last_name']
        