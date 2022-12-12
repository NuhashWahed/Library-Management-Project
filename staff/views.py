from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse
from . forms import BookForm,IssueBookForm, EditprofileForm
from django.contrib.auth.forms import UserChangeForm,PasswordChangeForm
from . models import Book,IssueBook
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate,update_session_auth_hash
from datetime import datetime, timedelta
from datetime import date
import datetime
# Create your views here.
def home(request):
    return render(request,"staff/home.html")


def userhome(request):
    return render(request,"staff/userhome.html")


def book(request):
    if request.method=="POST":
        form=BookForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                books=Book.objects.all()
                return render(request,'staff/show.html',{'books':books})
            except:
                pass
    else:
        form=BookForm()
    return render(request,'staff/index.html',{'form':form})  


def show(request):  
    books = Book.objects.all()  
    return render(request,"staff/show.html",{'books':books})


def update(request, id): 
     
    book = Book.objects.get(id=id)  
    form = BookForm(request.POST, instance = book) 
    if form.is_valid():  
        form.save()
        books = Book.objects.all()   
        return render(request,'staff/show.html',{'books':books}) 
    return render(request, 'staff/edit.html', {'book': book})  


def destroy(request, id):  
    book = Book.objects.get(id=id)  
    book.delete()  
    books = Book.objects.all()   
    return render(request,'staff/show.html',{'books':books})
    

def issuebook(request,id):
    x=Book.objects.get(id=id)
    if request.method=="POST":
        form=IssueBookForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                x.delete()
                books=IssueBook.objects.all()
                return render(request,'staff/issueshow.html',{'books':books})
            except:
                pass
    else:
        form=IssueBookForm()
    return render(request,'staff/issueindex.html',{'form':form})


def issuedestroy(request, id):  
    book = IssueBook.objects.get(id=id) 
    x=Book.objects.create(issn=book.bissn,bname=book.bname,bwritter=book.bwritter) 
    x.save()
    book.delete()  
    books = IssueBook.objects.all()   
    return render(request,'staff/issueshow.html',{'books':books}) 

def fine(request, id):
    book=IssueBook.objects.get(id=id)
    p1=datetime.date.today()+timedelta(days=3)
    p2=p1-datetime.date.today()
    d=0
    x=datetime.date.today()-book.submission_date
    
    delta=timedelta(days=1)
    while book.submission_date < datetime.date.today():
        d+=3
        
        book.submission_date += delta
    if x>(book.submission_date-book.submission_date):
        
        book.bname=d
    else:
        
        book.bname=0
        
   
    
     
    return render(request,'staff/fine.html',{'book':book}) 
    


def issueshow(request):  
    books = IssueBook.objects.all()  
    return render(request,"staff/issueshow.html",{'books':books})

def renew(request, id): 
     
    book = IssueBook.objects.get(id=id) 
    form = IssueBookForm(request.POST or None, instance = book) 
    print('out')
    if form.is_valid(): 
        print('in') 
        form.save()
        books = IssueBook.objects.all()   
        return render(request,'staff/issueshow.html',{'books':books}) 
    return render(request, 'staff/renew.html', {'book': book,'form':form})  


def showuser(request):
    User = get_user_model()
    users = User.objects.all()
    return render(request,"staff/showuser.html",{'users':users})


def destroyuser(request, username):
    u = User.objects.get(username=username)  
    u.delete()  
    users = User.objects.all()
    return render(request,"staff/showuser.html",{'users':users})


def register(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        confirm_password=request.POST['confirm_password']
        if password==confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username is already exist')
                return redirect(register)
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.set_password(password)
                user.save()
                return redirect("home")
    else:
        print("this is not post method")
    return render(request,"staff/register.html")


def editprofile(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            form=EditprofileForm(request.POST,instance=request.user)
            if form.is_valid:
                form.save()
                return redirect("userhome")
        else:
            fm=EditprofileForm(instance=request.user)
        return render(request,'staff/useredit.html',{'form':fm})
    else:
        return redirect('login_user')


def login_admin(request):
    if request.method== "POST":
        username=request.POST['username']
        password=request.POST['password']
        
        if username=='admin' and password=='admin':
            
            return redirect('show')
        else:
            print("invalid user")
    return render(request,"staff/admin_login.html")


def logout(request):
    auth.logout(request)
    return redirect('home')


def login_user(request):
    if request.method== "POST":
        username=request.POST['username']
        password=request.POST['password']
        x=auth.authenticate(username=username,password=password)  
        if x is not None:
            auth.login(request,x)
            return render(request,'staff/userhome.html')
        else:
            print("invalid user")
            return HttpResponse("invalid user")
    return render(request,"staff/user_login.html")


def studentissue(request):
    p=request.user.username
    x=IssueBook.objects.raw('SELECT * FROM issuebook WHERE sname=%s',[p])

    return render(request,"staff/studentissue.html",{'x':x})


def changepassword(request):
    if request.user.is_authenticated:
        if request.method =="POST":
            form=PasswordChangeForm(user=request.user, data=request.POST)
            if form.is_valid():
                form.save()
                update_session_auth_hash(request,form.user)
                return render(request,'staff/userhome.html')
        else:
           fm=PasswordChangeForm(user=request.user)
        return render(request,'staff/changepassword.html',{'form':fm})
    else:
        return redirect("login_user")

def search(request):
    if request.method =="POST":
        searched=request.POST['searched']
        
        x=Book.objects.filter(bname=searched)
        return render(request,'staff/search.html',{'searched':searched,'x':x})
    else:
        return render(request,'staff/search.html',{})




       

  
