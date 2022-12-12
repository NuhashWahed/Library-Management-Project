from django.db import models
from datetime import date, datetime

# Create your models here.
class Book(models.Model):  
    issn = models.CharField(max_length=20)  
    bname = models.CharField(max_length=100)  
    bwritter = models.CharField(max_length=15)  
    class Meta:  
        db_table = "book"  
class IssueBook(models.Model): 
    sname= models.CharField(max_length=100)
    sroll=models.CharField(max_length=100)
    sdept=models.CharField(max_length=100)
    bname = models.CharField(max_length=100)  
    bissn = models.CharField(max_length=15)
    bwritter = models.CharField(max_length=15)
    issue_date=models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    submission_date=models.DateField(auto_now_add=False,auto_now=False,blank=True,null=True)
    class Meta:  
        db_table = "issuebook"  
