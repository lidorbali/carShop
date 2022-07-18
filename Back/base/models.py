
 
from ast import And
from contextlib import nullcontext
from pickle import TRUE
from unicodedata import name
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
 
 
class Car(models.Model):
    user =models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    company=models.CharField(max_length=50,null=True,blank=True)
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.CharField(max_length=50,null=True,blank=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    _id=models.AutoField(primary_key=True,editable=False)




    def __str__(self):
           return self.company 
    

    