from datetime import datetime
from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from django.db import models
from operator import mod
import datetime

from numpy import product
from sqlalchemy import true

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class registeration(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    gender = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.firstname

    @staticmethod
    def gatemail(email):
        try:
            return registeration.objects.get(email = email)
        except:
            return False
class upload_product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to ='upload/product')
    price = models.IntegerField(default = 100)
    description = models.CharField(max_length=255 , default = "good")
    category = models.ForeignKey(Category, on_delete=models.CASCADE,default=1)

    def __str__(self):
        return self.name
class order(models.Model):
    product = models.ForeignKey(upload_product, on_delete=models.CASCADE)
    customer = models.ForeignKey(registeration , on_delete=models.CASCADE)
    quantity = models.IntegerField(default = 1)
    price = models.IntegerField()
    address = models.CharField(max_length=50 , default = "", blank=true)
    phone = models.IntegerField()
    date  = models.DateField(default = datetime.datetime.today)
    status = models.BooleanField(default = False)

class demodb(models.Model):
    name = models.CharField(max_length= 50)
    email = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

