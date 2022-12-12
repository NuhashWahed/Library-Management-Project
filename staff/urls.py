from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
  
    path('book/',views.book, name='book'),
    path('show/',views.show, name='show'),
    path('update/<int:id>/', views.update, name='update'),  
    path('delete/<int:id>/', views.destroy, name='delete'), 
    path('issuedelete/<int:id>/', views.issuedestroy, name='issuedelete'),
    path('issuebook/<int:id>/',views.issuebook, name='issuebook'),
    path('issueshow/',views.issueshow, name='issueshow'),
  path('showuser/',views.showuser, name='showuser'),
  path('userdelete/<str:username>/', views.destroyuser, name='userdelete'),
  path('register/',views.register, name='register'),
  path('editprofile',views.editprofile, name='editprofile'),
  path('',views.home, name='home'),
  path('login_admin/',views.login_admin, name='login_admin'),
  path('logout/',views.logout, name='logout'),
    path('login_user/',views.login_user, name='login_user'),
    path('studentissue/',views.studentissue, name='studentissue'),
    path('changepassword/',views.changepassword, name='changepassword'),
    
    path('userhome/',views.userhome, name='userhome'),
    path('renew/<int:id>/',views.renew, name='renew'),
  path('search',views.search, name='search'),
  path('fine/<int:id>/',views.fine, name='fine'),
  
]
