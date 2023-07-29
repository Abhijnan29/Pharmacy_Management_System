from django.db import models
from datetime import timezone

# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.

class contact(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phoneno=models.CharField(max_length=10,null=True)
    desc=models.TextField()

    def __str__(self):
        return self.email


class Med_Prod(models.Model):
    medicine_name=models.CharField(max_length=250,null=True)
    medicine_image=models.ImageField(upload_to="Med_Prod",blank=True,null=True)
    medicine_price=models.IntegerField(null=True)
    medicine_descripton=models.TextField(null=True)
    medicine_exp=models.DateField(null=True)
    prod_name=models.CharField(max_length=250,null=True)
    prod_image=models.ImageField(upload_to="Med_Prod",blank=True,null=True)
    prod_price=models.IntegerField(null=True)
    prod_descripton=models.TextField(null=True)
    prod_exp=models.DateField(null=True)
    
    def __str__(self):
        return self.medicine_name
        return self.prod_name


class order(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    items=models.CharField(max_length=1500)
    address=models.TextField()
    quantity=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
    phone_num=models.CharField(max_length=10)
    delivery=models.BooleanField(default=False)
    def __int__(self):
        return self.id
